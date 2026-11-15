#!/usr/bin/env node
/**
 * Build the required seven-column research ledger.
 *
 * Usage, in an OS temporary directory with a node_modules symlink pointing to
 * CODEX_PRIMARY_RUNTIME_NODE_MODULES:
 *   "$CODEX_PRIMARY_RUNTIME_NODE" build_totex_results.mjs /absolute/deliverables
 *
 * Inputs: TOTEX_paper.tex, code/totex_results_metadata.json, and either
 * TOTEX_paper.aux or the exact code/totex_labels_cache.json supplied here.
 * An authoring tree with input files sections/A.tex through F.tex also works.
 * Final flattened TeX is preferred and needs no sections directory.
 *
 * Spreadsheet authoring uses @oai/artifact-tool. The documented API exposes
 * CSV import but no CSV export. The authored/recalculated worksheet values
 * are read back and serialized as RFC 4180 CSV. No XLSX is created.
 */
import fs from "node:fs/promises";
import path from "node:path";
import crypto from "node:crypto";
import assert from "node:assert/strict";
import { Workbook } from "@oai/artifact-tool";

const root = path.resolve(process.argv[2] ?? ".");
const outputDir = path.join(root, "code", "outputs");
await fs.mkdir(outputDir, { recursive: true });
const metadataFile = path.join(root, "code", "totex_results_metadata.json");
const metadataText = await fs.readFile(metadataFile, "utf8");
const metadata = JSON.parse(metadataText);
const columns = [
  "id", "statement", "status", "where_proved", "depends_on",
  "manuscript_pages_settled", "notes",
];
assert.deepEqual(metadata.columns, columns, "The requested schema is exact.");
const allowed = new Set(["Proved", "Refuted", "Known", "Open"]);
const environments = [
  "theorem", "proposition", "lemma", "corollary", "definition",
  "example", "obstruction", "audit", "remark",
];
const envNames = environments.join("|");
const beginPattern = "\\\\begin\\{(" + envNames + ")\\}(?:\\[([\\s\\S]*?)\\])?";
const sha256 = value => crypto.createHash("sha256").update(value).digest("hex");
const readSources = [];
const sourceUnicodeScans = [];
async function readInput(filename) {
  const absolute = path.resolve(root, filename);
  assert(absolute.startsWith(root + path.sep), "Source must stay in deliverable tree.");
  const text = await fs.readFile(absolute, "utf8");
  const controls = [...text.matchAll(/[\u0000-\u0009\u000B\u000C\u000E-\u001F\u007F]/g)];
  const replacements = [...text.matchAll(/\uFFFD/g)];
  const bidi = [...text.matchAll(/[\u202A-\u202E\u2066-\u2069]/g)];
  sourceUnicodeScans.push({
    file: path.relative(root, absolute),
    unexpected_control_count: controls.length,
    unicode_replacement_character_count: replacements.length,
    bidirectional_format_control_count: bidi.length,
  });
  assert.equal(controls.length, 0, "Unexpected source control character in " + filename);
  assert.equal(replacements.length, 0, "Unicode replacement character in " + filename);
  assert.equal(bidi.length, 0, "Unexpected bidirectional format control in " + filename);
  readSources.push({ file: path.relative(root, absolute), sha256: sha256(text) });
  return text;
}
const paper = await readInput("TOTEX_paper.tex");
let sources;
if (new RegExp(beginPattern).test(paper)) {
  sources = [{ file: "TOTEX_paper.tex", text: paper }];
} else {
  sources = [];
  for (const section of "ABCDEF") {
    const filename = "sections/" + section + ".tex";
    sources.push({ file: filename, text: await readInput(filename) });
  }
}
const statements = [];
for (const source of sources) {
  const beginnings = [...source.text.matchAll(new RegExp(beginPattern, "g"))];
  for (let i = 0; i < beginnings.length; i++) {
    const match = beginnings[i];
    const [startToken, environment, title = ""] = match;
    const start = match.index;
    const bodyStart = start + startToken.length;
    const endToken = "\\end{" + environment + "}";
    const end = source.text.indexOf(endToken, bodyStart);
    assert(end >= 0, "Unclosed " + environment + " at " + source.file + ":" + start);
    const body = source.text.slice(bodyStart, end);
    const labels = [...body.matchAll(/\\label\{([^}]+)\}/g)].map(x => x[1]);
    assert.equal(labels.length, 1, "Expected one statement label: " + title);
    const next = beginnings[i + 1]?.index ?? source.text.length;
    const after = source.text.slice(end + endToken.length, next);
    const proofMatch = /\\begin\{proof\}(?:\[[\s\S]*?\])?/.exec(after);
    let proof = "";
    if (proofMatch) {
      const proofEnd = after.indexOf("\\end{proof}", proofMatch.index);
      assert(proofEnd >= 0, "Unclosed proof after " + labels[0]);
      proof = after.slice(proofMatch.index, proofEnd + "\\end{proof}".length);
    }
    const refMentions = [...new Set(
      [...(body + proof).matchAll(/\\ref\{([^}]+)\}/g)].map(x => x[1])
    )];
    const citationMentions = [...new Set(
      [...(body + proof).matchAll(/\\cite\w*(?:\[[^\]]*\])*\{([^}]+)\}/g)]
        .flatMap(x => x[1].split(",").map(y => y.trim()))
    )];
    statements.push({
      label: labels[0], environment, title, file: source.file,
      source_line: source.text.slice(0, start).split("\n").length,
      statement_tex: body.trim(), proof_tex: proof.trim(),
      ref_mentions: refMentions, citation_mentions: citationMentions,
    });
  }
}
const labels = statements.map(x => x.label);
assert.equal(new Set(labels).size, labels.length, "Duplicate numbered labels.");
const metadataLabels = Object.keys(metadata.statements);
assert.deepEqual([...labels].sort(), [...metadataLabels].sort(),
  "Metadata must cover every and only numbered statements.");

const aux = new Map();
const labelCacheFile = path.join(root, "code", "totex_labels_cache.json");
let numberingInput;
try {
  const auxText = await fs.readFile(path.join(root, "TOTEX_paper.aux"), "utf8");
  for (const match of auxText.matchAll(/^\\newlabel\{([^}]+)\}\{\{([^{}]+)\}\{([^{}]+)\}/gm)) {
    assert(!aux.has(match[1]), "Duplicate aux label " + match[1]);
    aux.set(match[1], { id: match[2], page: match[3] });
  }
  numberingInput = { file: "TOTEX_paper.aux", sha256: sha256(auxText) };
  await fs.writeFile(labelCacheFile, JSON.stringify({
    source: "TOTEX_paper.aux", aux_sha256: sha256(auxText),
    labels: Object.fromEntries(aux),
  }, null, 2) + "\n");
} catch (error) {
  if (error.code !== "ENOENT") throw error;
  const cacheText = await fs.readFile(labelCacheFile, "utf8");
  const cache = JSON.parse(cacheText);
  for (const [label, value] of Object.entries(cache.labels)) aux.set(label, value);
  numberingInput = { file: "code/totex_labels_cache.json", sha256: sha256(cacheText),
    cached_aux_sha256: cache.aux_sha256 };
}
const auxTheoremLabels = [...aux.entries()]
  .filter(([, x]) => /^[A-F]\.\d+$/.test(x.id))
  .map(([label]) => label);
assert.deepEqual([...labels].sort(), auxTheoremLabels.sort(),
  "Aux theorem labels must exactly match the parsed numbered statements.");

const statusCounts = { Proved: 0, Refuted: 0, Known: 0, Open: 0 };
const sectionCounts = {};
const coverage = Object.fromEntries(metadata.required_request_tags.map(x => [x, []]));
const sourceRecords = [];
const rows = [];
const previousNumber = {};
const ids = [];
for (const item of statements) {
  const m = metadata.statements[item.label];
  const location = aux.get(item.label);
  assert(location, "Missing aux label " + item.label);
  const { id, page } = location;
  assert(/^[A-F]\.\d+$/.test(id), "Invalid numbered id " + id);
  assert(/^\d+$/.test(page), "Invalid PDF start page " + page);
  const [section, ordinal] = id.split(".");
  assert.equal(Number(ordinal), (previousNumber[section] ?? 0) + 1,
    "Nonconsecutive statement numbering in section " + section);
  previousNumber[section] = Number(ordinal);
  sectionCounts[section] = (sectionCounts[section] ?? 0) + 1;
  ids.push(id);

  const headingStatus = /^(Proved|Refuted|Known|Open)\b/.exec(item.title)?.[1];
  assert(headingStatus, "No permitted status heading: " + item.label);
  assert(allowed.has(m.status), "Unnormalized status: " + item.label);
  assert.equal(m.status, headingStatus, "Status disagrees with TeX: " + item.label);
  assert(m.statement.length > 65, "Insufficient descriptive statement: " + item.label);
  assert(m.notes.length > 40, "Missing substantive notes: " + item.label);
  if (/Refuted and repaired/.test(item.title)) {
    assert(/repair/i.test(m.notes), "Repair not stated: " + item.label);
  }
  const dependencyLabels = m.internal ?? [];
  for (const dependency of dependencyLabels) {
    assert(metadata.statements[dependency], "Unresolved dependency " + dependency);
    assert.notEqual(dependency, item.label, "Self dependency.");
  }
  const dependencies = [
    ...dependencyLabels.map(label => aux.get(label).id + " (" + label + ")"),
    ...(m.external ?? []),
  ];
  assert(dependencies.length > 0, "No proof ingredients supplied: " + item.label);
  const type = item.environment[0].toUpperCase() + item.environment.slice(1);
  const locationText = "TOTEX_paper.pdf, " + type + " " + id + ", p. " + page +
    "; TOTEX_paper.tex, label " + item.label;
  const requestText = "Prompt coverage: " + m.requests.join(", ") + ". ";
  const notes = "Label " + item.label + ". " + requestText + m.notes;
  const row = [
    id, m.statement, m.status, locationText, dependencies.join("; "),
    m.manuscript_pages_settled ?? "", notes,
  ];
  for (const [index, value] of row.entries()) {
    assert.equal(typeof value, "string", "Nontext value " + item.label + ", " + columns[index]);
    assert(!/^[=+@]/.test(value), "Unexpected spreadsheet formula prefix.");
    assert(!/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/.test(value),
      "Unexpected control character.");
  }
  rows.push(row);
  statusCounts[m.status]++;
  for (const tag of m.requests) {
    assert(tag in coverage, "Unknown request tag " + tag);
    coverage[tag].push({ id, label: item.label, status: m.status });
  }
  sourceRecords.push({
    ...item, id, pdf_start_page: Number(page), normalized_status: m.status,
    curated_internal_dependencies: dependencyLabels,
    curated_external_dependencies: m.external ?? [],
    request_tags: m.requests,
  });
}
for (const [tag, mapped] of Object.entries(coverage)) {
  assert(mapped.length > 0, "Dropped user-request item " + tag);
}
assert.equal(new Set(ids).size, ids.length, "Duplicate CSV ids.");
assert.equal(rows.length, statements.length);

const workbook = Workbook.create();
const sheet = workbook.worksheets.add("Results");
const matrix = [columns, ...rows];
const extent = "A1:G" + matrix.length;
sheet.getRange(extent).values = matrix;
sheet.getRange(extent).format.numberFormat = "@";
sheet.getRange(extent).format.font = { name: "Arial", size: 10 };
sheet.getRange(extent).format.wrapText = true;
sheet.getRange(extent).format.verticalAlignment = "top";
sheet.showGridLines = false;
sheet.getRange("A1:G1").format = {
  fill: "#18344B",
  font: { name: "Arial", size: 10, bold: true, color: "#FFFFFF" },
  wrapText: true,
  verticalAlignment: "center",
  horizontalAlignment: "center",
};
const columnWidths = [74, 760, 88, 380, 760, 380, 850];
for (let c = 0; c < 7; c++) {
  const letter = String.fromCharCode(65 + c);
  sheet.getRange(letter + "1:" + letter + matrix.length).format.columnWidthPx = columnWidths[c];
}
sheet.getRange("A1:G1").format.rowHeightPx = 40;
for (let r = 2; r <= matrix.length; r++) {
  const sourceRow = matrix[r - 1];
  const maxLines = Math.max(...sourceRow.map((x, c) =>
    Math.ceil(x.length / Math.floor(columnWidths[c] / 6.5))));
  sheet.getRange("A" + r + ":G" + r).format.rowHeightPx = Math.max(68, 17 * maxLines + 12);
  if (r % 2 === 0) sheet.getRange("A" + r + ":G" + r).format.fill = "#F1F5F8";
}
sheet.freezePanes.freezeRows(1);
sheet.freezePanes.freezeColumns(1);
workbook.recalculate();

const readback = sheet.getRange(extent).values.map(row =>
  row.map(value => value === null || value === undefined ? "" : String(value))
);
assert.deepEqual(readback, matrix, "Artifact worksheet readback changed table data.");
const inspect = await workbook.inspect({
  kind: "table", range: "Results!A1:G4", include: "values,formulas",
  tableMaxRows: 4, tableMaxCols: 7, maxChars: 14000,
});
await fs.writeFile(path.join(outputDir, "totex_results_inspect.ndjson"), inspect.ndjson + "\n");
const formulaCells = await workbook.inspect({
  select: "$.sheets[*].cells[?(@.formula)]",
  include: ["sheet", "address", "formula"],
});
assert.equal(formulaCells.records.length, 0, "The text-only ledger contains a formula.");

function encodeCSV(data) {
  const quote = value => '"' + value.replaceAll('"', '""') + '"';
  return data[0].join(",") + "\r\n" +
    data.slice(1).map(row => row.map(quote).join(",")).join("\r\n") + "\r\n";
}
function parseCSV(csv) {
  const parsed = [];
  let row = [], value = "", quoted = false;
  for (let i = 0; i < csv.length; i++) {
    const char = csv[i];
    if (quoted) {
      if (char === '"') {
        if (csv[i + 1] === '"') { value += '"'; i++; }
        else quoted = false;
      } else value += char;
    } else if (char === '"') quoted = true;
    else if (char === ",") { row.push(value); value = ""; }
    else if (char === "\r" && csv[i + 1] === "\n") {
      row.push(value); parsed.push(row); row = []; value = ""; i++;
    } else if (char === "\n") {
      row.push(value); parsed.push(row); row = []; value = "";
    } else value += char;
  }
  assert(!quoted, "Unclosed CSV quote.");
  if (value.length || row.length) { row.push(value); parsed.push(row); }
  return parsed;
}
const csv = encodeCSV(readback);
const csvFile = path.join(root, "TOTEX_results.csv");
await fs.writeFile(csvFile, csv, "utf8");
const saved = await fs.readFile(csvFile, "utf8");
assert.deepEqual(parseCSV(saved), matrix, "RFC 4180 parse roundtrip changed data.");
const imported = await Workbook.fromCSV(saved, { sheetName: "Reopened" });
const importedValues = imported.worksheets.getItem("Reopened")
  .getRange(extent).values.map(row =>
    row.map(value => value === null || value === undefined ? "" : String(value)));
assert.deepEqual(importedValues, matrix, "Artifact CSV-import roundtrip changed data.");

const preview = await workbook.render({
  sheetName: "Results", range: "A1:C5", scale: 1, format: "png",
});
await fs.writeFile(path.join(outputDir, "totex_results_preview.png"),
  new Uint8Array(await preview.arrayBuffer()));

const audits = {
  artifact_authoring: true,
  spreadsheet_output: "CSV only; no XLSX created",
  csv_serializer: "RFC 4180 from recalculated artifact-tool worksheet readback",
  exact_columns: columns,
  numbered_statement_count: statements.length,
  csv_data_row_count: rows.length,
  status_counts: statusCounts,
  section_counts: sectionCounts,
  missing_metadata: [],
  extra_metadata: [],
  unresolved_internal_dependencies: [],
  duplicate_ids: [],
  status_mismatches: [],
  formula_cell_count: formulaCells.records.length,
  complete_statement_coverage: true,
  complete_prompt_item_coverage: true,
  exact_artifact_worksheet_readback: true,
  exact_csv_parser_roundtrip: true,
  exact_artifact_csv_import_roundtrip: true,
  unicode_csv_roundtrip_preserved: true,
  source_unicode_control_scans: sourceUnicodeScans,
  preview: "code/outputs/totex_results_preview.png (first four statements, A–C columns)",
  source_mode: sources.length === 1 ? "flattened-paper" : "authoring-sections",
  inputs: [
    ...readSources,
    numberingInput,
    { file: "code/totex_results_metadata.json", sha256: sha256(metadataText) },
  ],
  csv_sha256: sha256(saved),
  manuscript_page_policy: "Only actual manuscript assertions addressed are mapped. Research-only and unresolved statements have blank manuscript_pages_settled; current PDF start pages are in where_proved.",
  source_access_scope: {
    bodies_not_opened: ["Oberst (1968)", "Isbell–Mitchell (1976)", "Gabriel–Ulmer (1971)"],
    ledger_row: aux.get("F:source-access").id,
    mathematical_dependencies_use_unopened_bodies: false,
  },
  important_limitations: [
    "The integral, rational, and prime-field total⇒exact implications remain unresolved.",
    "K1 has computed H2=Z and it injects into full K2; full K2 rank was not enumerated (92,089 objects in the chosen convention).",
    "K3 and infinite-union persistence remain unresolved; selected substages are not full stages.",
    "A separate literal-common-n general B.9 substage has verified rank-one H2 class death; its full specified K2 and infinite completion remain unresolved. It is not a C.1 stage.",
    "The terminal-object modification is minimal only among proper full extensions measured by added-object count.",
    "The final-image exclusion in Part E covers finite products and finite iterations.",
    "The literature comparison with three inaccessible source bodies is explicitly open.",
  ],
  request_coverage: coverage,
  provenance: metadata.provenance,
};
await fs.writeFile(path.join(outputDir, "totex_results_source_records.json"),
  JSON.stringify(sourceRecords, null, 2) + "\n");
await fs.writeFile(path.join(outputDir, "totex_results_audit.json"),
  JSON.stringify(audits, null, 2) + "\n");
await fs.writeFile(path.join(outputDir, "totex_results_values.json"),
  JSON.stringify(matrix, null, 2) + "\n");
console.log(JSON.stringify({
  csv: csvFile, rows: rows.length, columns, status_counts: statusCounts,
  section_counts: sectionCounts, source_mode: audits.source_mode,
  checks: "all passed",
  audit: path.join(outputDir, "totex_results_audit.json"),
}, null, 2));

