"""Record exact source theorem counters and finite computation summaries.
Run from the workspace root containing sources/ and PATHS/. No network needed.
The source has one numbered align in section 1 and one numbered equation in
section 3, sharing the theorem counter; the scanner counts these as well.
"""
import re,json
from pathlib import Path
src=Path('sources/papers/2608.19870/hammock_4.tex').read_text()
rx=re.compile(r'\\section(\*?)\{|\\begin\{(thm|prop|cor|defn|rem|notation|example|construction|lem|convention|equation|align)\}|\\label\{([^}]+)\}')
targets={'thm:Z_Segal','cor:hammock_anima_is_anima_of_loc','prop:infinity_1_colimit','thm:comparison','def:hammock','thm:fibrationcats','thm:fraction','def:hammock_DK','lem:Zigpartial_cof_const'}
sec=num=0;kind=''
for m in rx.finditer(src):
 if m.group(1)is not None:
  if m.group(1)=='':sec+=1;num=0
 elif m.group(2):num+=1;kind=m.group(2)
 elif m.group(3) in targets:
  print(json.dumps({'source':'ArakawaCnossen supplied LaTeX','label':m.group(3),'number':f'{sec}.{num}','environment':kind}))
for L in (3,4):
 rows=[json.loads(s)for s in Path(f'PATHS/code/b_path_search_L{L}.jsonl').read_text().splitlines()]
 cases=[x for x in rows if 'same_h0_h1' in x]
 print(json.dumps({'max_word_length':L,'comparisons':len(cases),'h0_h1_discrepancies':sum(not x['same_h0_h1'] for x in cases),'largest_arrow_count':max(x[k]['nonidentity_arrows']for x in cases for k in ('full','restricted')),'largest_2simplex_count':max(x[k]['nondegenerate_2simplices']for x in cases for k in ('full','restricted'))}))
