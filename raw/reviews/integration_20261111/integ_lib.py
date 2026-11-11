"""Shared functions for the integration of the Pro answers POLES, GALOIS, STRATA, PATHS, BISITE into the companion's
checked files (checks/DER_<id>/). Same method as apply_integration.py (CATHOT, TOTASPH), plus:
  %%APPEND title="<existing block>"   adds the paragraphs that follow at the end of that block;
  before/ keeps the first original of each file (never overwritten); before/<PACKAGE>/ keeps the state of each file
  just before that package touched it.
Each apply_<PACKAGE>.py is run once:  python -I apply_<PACKAGE>.py   (python -I: this folder is not on the path, so the
scripts add it themselves)."""
import csv
import io
import pathlib
import re
import shutil
import sys

sys.stdout.reconfigure(encoding='utf-8')
HERE = pathlib.Path(__file__).parent
CHK = HERE.parent.parent / 'checks'
BLOCK = re.compile(r'\\begin\{dcomment\}\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}(.*?)\\end\{dcomment\}', re.S)


class Run:
    def __init__(self, package, review):
        self.pkg = package
        self.log = []
        self.note = ('Pro answer ' + package + ' (AI-produced by GPT-6 Astra, OpenAI, ChatGPT Pro mode), {n}; reviewed by '
                     'Claude (Fable 5.2, Anthropic), pro_reviews_20261110/' + review + ', 11 Nov 2026{v}.')
        self.touched = set()

    def N(self, n, v=''):
        """notes text: statement numbers n; v = verdict words, e.g. 'followed' or 'unverified'."""
        return self.note.format(n=n, v=(': ' + v) if v else '')

    def backup(self, path):
        if path in self.touched:
            return
        self.touched.add(path)
        first = HERE / 'before' / path.name
        if not first.exists():
            shutil.copy2(path, first)
        d = HERE / 'before' / self.pkg
        d.mkdir(exist_ok=True)
        if not (d / path.name).exists():
            shutil.copy2(path, d / path.name)

    def rw(self, path, fn):
        self.backup(path)
        raw = path.read_bytes()
        crlf = b'\r\n' in raw
        s = raw.decode('utf-8').replace('\r\n', '\n')
        s2 = fn(s)
        assert s2 != s, path
        path.write_bytes((s2.replace('\n', '\r\n') if crlf else s2).encode('utf-8'))

    def blocks_edit(self, cid, newfile, paragraph_repl=()):
        path = CHK / f'DER_{cid}' / f'DER_{cid}_blocks.tex'
        new = (HERE / newfile).read_text(encoding='utf-8') if newfile else ''
        if new.startswith('%%FILE '):   # one file for several chunks: sections headed by a line %%FILE <id>
            secs = re.split(r'^%%FILE (\S+)\n', new, flags=re.M)
            new = ''.join(secs[k + 1] for k in range(1, len(secs), 2) if secs[k] == cid)
            assert new.strip(), (newfile, cid)
        parts = re.split(r'^%%(BLOCK|REPLACE|APPEND) (after|title)="([^"]*)"\n', new, flags=re.M)
        assert not parts[0].strip(), parts[0][:80]
        log = self.log

        def fn(s):
            for k in range(1, len(parts), 4):
                mode, title, body = parts[k], parts[k + 2], parts[k + 3].strip() + '\n'
                hits = [m for m in BLOCK.finditer(s) if m.group(1 + 2).strip() == title]
                assert len(hits) == 1, (cid, title, len(hits))
                m = hits[0]
                if mode == 'APPEND':
                    assert '\\begin{dcomment}' not in body, title
                    assert body.strip()[:60] not in s, ('already applied', title)
                    if '\\ours' in body:
                        assert m.group(1).strip() == 'development', (title, 'ours outside development')
                    end = m.end() - len('\\end{dcomment}')
                    s = s[:end].rstrip('\n') + '\n\n' + body.rstrip('\n') + '\n' + s[end:]
                    log.append(f'{cid}: block "{title}" extended ({len(body.split())} words added at its end)')
                    continue
                for nb in BLOCK.finditer(body):
                    assert not any(x.group(3).strip() == nb.group(3).strip() for x in BLOCK.finditer(s)) or mode == 'REPLACE', \
                        ('already applied', nb.group(3))
                    log.append(f'{cid}: {"replaced block" if mode == "REPLACE" else "new block"} "{nb.group(3)}"'
                               + (f' (was "{title}")' if mode == 'REPLACE' else f' after "{title}"'))
                assert body.count('\\begin{dcomment}') == body.count('\\end{dcomment}') == len(BLOCK.findall(body)) >= 1, title
                if mode == 'BLOCK':
                    s = s[:m.end()] + '\n\n' + body.rstrip('\n') + s[m.end():]
                else:
                    s = s[:m.start()] + body.rstrip('\n') + s[m.end():]
            for old, newp in paragraph_repl:
                assert s.count(old) == 1, (cid, s.count(old), old[:80])
                s = s.replace(old, newp)
                log.append(f'{cid}: paragraph updated: "{old[:70]}..."')
            return s
        self.rw(path, fn)

    def rows_edit(self, cid, edits):
        path = CHK / f'DER_{cid}' / f'DER_{cid}_claims.csv'
        self.backup(path)
        raw = path.read_bytes()
        crlf = b'\r\n' in raw
        rows = list(csv.reader(io.StringIO(raw.decode('utf-8'), newline='')))
        ix = {h: i for i, h in enumerate(rows[0])}
        seen = set()
        for r in rows[1:]:
            if r and r[0] in edits:
                seen.add(r[0])
                for col, val in edits[r[0]].items():
                    if col.endswith('+'):
                        c = col[:-1]
                        assert val[:50] not in r[ix[c]], ('already applied', r[0])
                        r[ix[c]] = (r[ix[c]].rstrip() + ' ' + val).strip()
                    else:
                        r[ix[col]] = val
                self.log.append(f'{cid}: row {r[0]} updated ({", ".join(edits[r[0]])}); proof_status now "{r[ix["proof_status"]]}"')
        assert seen == set(edits), set(edits) - seen
        out = io.StringIO(newline='')
        csv.writer(out, lineterminator='\r\n' if crlf else '\n').writerows(rows)
        path.write_bytes(out.getvalue().encode('utf-8'))

    def bib_add(self, cid, entries):
        path = CHK / f'DER_{cid}' / f'DER_{cid}_references.bib'

        def fn(s):
            for entry in entries:
                key = re.match(r'\s*@\w+\{([^,]+),', entry).group(1)
                if re.search(r'@\w+\s*\{\s*' + re.escape(key) + r'\s*,', s):
                    continue
                s = s.rstrip('\n') + '\n\n' + entry.strip() + '\n'
                self.log.append(f'{cid}: bibliography entry {key} added')
            return s
        try:
            self.rw(path, fn)
        except AssertionError:
            pass   # every key was already there

    def overview_append(self, cid, text):
        """Add paragraphs at the end of DER_<id>_overview.tex (before a closing otherlanguage environment)."""
        path = CHK / f'DER_{cid}' / f'DER_{cid}_overview.tex'
        text = text.strip()

        def fn(s):
            assert text[:60] not in s, ('already applied', cid)
            m = re.search(r'\n\\end\{otherlanguage\*?\}\s*$', s)
            if m:
                return s[:m.start()].rstrip('\n') + '\n\n' + text + '\n' + s[m.start():]
            return s.rstrip('\n') + '\n\n' + text + '\n'
        self.rw(path, fn)
        self.log.append(f'{cid}: overview extended ({len(text.split())} words)')

    def finish(self, items):
        """Append this package's section to INTEGRATION_LOG.md. items: free text lines (list item by list item)."""
        p = HERE / 'INTEGRATION_LOG.md'
        s = p.read_text(encoding='utf-8').rstrip('\n')
        s += (f'\n\n# Integration of {self.pkg} (11 November 2026)\n\nApplied by `apply_{self.pkg}.py` '
              f'(with `integ_lib.py`). State of each file before this package: `before\\{self.pkg}\\`.\n\n'
              + '\n'.join('- ' + l for l in self.log) + '\n\n## ' + self.pkg + ': the review\'s list, item by item\n\n'
              + '\n'.join('- ' + l for l in items) + '\n')
        p.write_text(s, encoding='utf-8', newline='\r\n')
        print('\n'.join(self.log))
