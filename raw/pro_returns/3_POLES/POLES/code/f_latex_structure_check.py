"""Check section-level TeX environment and display delimiters before compilation.

This is a syntax diagnostic, not a proof checker.  LuaLaTeX remains authoritative.
"""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parents[1]
results = []
for path in sorted((root / 'sections').glob('*.tex')):
    stack = []
    problems = []
    text = re.sub(r'(?<!\\)%[^\n]*', '', path.read_text())
    pattern = r'\\begin\{([^}]+)\}|\\end\{([^}]+)\}|(?<!\\)\\\[|(?<!\\)\\\]'
    for match in re.finditer(pattern, text):
        line = text.count('\n', 0, match.start()) + 1
        token = match.group()
        if match.group(1):
            stack.append(('environment', match.group(1), line))
        elif token == r'\[':
            stack.append(('display', 'display', line))
        else:
            expected = ('environment', match.group(2)) if match.group(2) else ('display', 'display')
            if not stack or stack[-1][:2] != expected:
                problems.append({'line': line, 'unexpected_close': token, 'stack': stack.copy()})
            else:
                stack.pop()
    if stack:
        problems.append({'unclosed': stack})
    results.append({'file': str(path.relative_to(root)), 'problems': problems})
(root / 'code' / 'f_latex_structure_check_output.json').write_text(json.dumps(results, indent=2) + '\n')
for item in results:
    print(item['file'], ':', 'balanced' if not item['problems'] else json.dumps(item['problems']))
