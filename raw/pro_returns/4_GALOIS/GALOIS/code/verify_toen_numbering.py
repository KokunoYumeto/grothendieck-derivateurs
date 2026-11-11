"""Recover theorem numbers from the supplied Toën LaTeX source, no compilation."""
import re
from pathlib import Path
p=Path('background/papers/math_0012219/math_0012219.tex')
s=p.read_text()
s=re.sub(r'(?m)(?<!\\)%.*$','',s)
pat=re.compile(r'\\setcounter\{section\}\{(-?\d+)\}|\\section\{|\\subsection\{|\\begin\{(thm|prop|lem|df|cor|conj)\}(?:\s*\\label\{([^}]+)\})?')
a=b=c=0
for m in pat.finditer(s):
 t=m.group()
 if m.group(1): a=int(m.group(1))
 elif t.startswith('\\section'): a+=1;b=c=0
 elif t.startswith('\\subsection'): b+=1;c=0
 else:
  c+=1
  if a==3 and b==3:print(f'{a}.{b}.{c}', m.group(2), m.group(3) or '(unlabelled)')
