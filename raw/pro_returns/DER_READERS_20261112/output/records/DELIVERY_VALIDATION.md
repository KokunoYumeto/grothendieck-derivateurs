# Delivery validation

**Status: pass.**

The validation binds the source plans, annotated masters, standalone sources, compiled PDFs, and delivery payload by SHA-256. All paths are archive-relative.

| PDF | Pages | Full-page text and metadata scanned |
|---|---:|---|
| `DER_FR_diplomatique` | 915 | Yes |
| `DER_FR_corrige_apparat` | 1082 | Yes |
| `DER_FR_texte_de_lecture` | 899 | Yes |
| `DER_FR_annotated_master` | 915 | Yes |
| `DER_EN_diplomatic` | 915 | Yes |
| `DER_EN_corrected_apparatus` | 1061 | Yes |
| `DER_EN_reading` | 902 | Yes |
| `DER_EN_annotated_master` | 915 | Yes |
| `LesDerivateurs_companion` | 1906 | Yes |

## Apparatus links

| Language | Expected destinations | Verified destination and one visible inbound marker |
|---|---:|---:|
| FR | 1982 | 1982 |
| EN | 1623 | 1623 |

Every expected ID must occur once in the PDF destination name tree, resolve to a page, and receive exactly one link annotation whose rectangle contains that visible marker ID. Per-ID evidence is in `DELIVERY_APPARATUS_LINKS.tsv`.

## Default master projections

- FR: exact; 915 pages compared, including each page’s exact extracted text and geometry.
- EN: exact; 915 pages compared, including each page’s exact extracted text and geometry.

## Final margin-repair evidence

The six standalone margin audits pass with zero confirmed collisions and zero unreviewed candidates. All six repaired labels have positive horizontal clearance. The refinement comparison is bound to the current eight PDF, TeX, and compile-record hashes; it covers 7604 pages, permits exactly one specified label translation per book, and confirms identical pixels and dimensions for all 68 reviewed samples.

## Privacy and payload

Privacy findings: **0**. Full payload text, all PDF pages, PDF metadata, and link URIs are scanned. Detection regular expressions and generic runtime constants in code are classified separately; private values are never copied into this report.

The whitelist excludes generated TeX auxiliary files, raw reader logs, caches, preview images, glyph-debug material, stale files, and preliminary delivery reports. Language archives contain exactly four `.tex` and four `.pdf` files plus their root README. The records archive contains the approved records and companion source tree.

The final manifest records archive name, archive-relative member path, byte length, and SHA-256. It includes the completed validation reports. `DELIVERY_MANIFEST.tsv` excludes its own row to avoid self-reference; the archive receipt outside the ZIPs records each complete archive’s SHA-256 and protects the manifest as an archive member.

## Pending release records

None.

## Issues

None.
