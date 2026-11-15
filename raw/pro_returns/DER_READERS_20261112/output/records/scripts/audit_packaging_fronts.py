#!/usr/bin/env python3
"""Check the six compiled front matters and scan their complete PDF text.

The repository credit roles were compared by human reading. This replay checks
their emitted front text, exact rights paragraphs, required credit tokens,
compiled title and credit pages, immutable build hashes, and privacy patterns.
Only audit records are written; reader sources and PDFs are read unchanged.
"""
from pathlib import Path
import hashlib,json,re,subprocess
import fitz
import build_readers as B
from validate_delivery import privacy_scan

ROOT=Path(__file__).resolve().parents[3]
RECORDS=ROOT/'output/records'
COMMON=['Alexander Grothendieck','Künzer','Malgoire','Maltsiniotis',
        'Opus~5.5','Fable~5.2','GPT-6 Astra','GPT-6.1 Sol',
        'OpenAI, ChatGPT Pro mode','AI-transcribed','AI-translated',
        'AI-produced corrections']
TITLES={'FR':['Texte diplomatique','Texte corrigé avec apparat','Texte de lecture'],
        'EN':['Diplomatic text','Corrected text with apparatus','Plain reading text']}
FORBIDDEN=re.compile(r'AI[\s\-‐‑–]+assisted',re.I)
ROLES=[
    'Alexander Grothendieck as author; Künzer–Malgoire–Maltsiniotis edition, deciphering, and ownership of editors’ notes',
    'Claude Opus 5.5 (Anthropic) for the AI-transcribed text',
    'GPT-6 Astra for the companion commentary, claims register, and corrections; Claude Opus 5.5 for checking and integration',
    'Claude Fable 5.2 for reviewed-answer contributions: eight blocks, seven paragraphs, nineteen register rows, and three bibliography entries',
    'Claude Opus 5.5 for macro-definition and unlisted transcription corrections compared against edition pages',
    'GPT-6.1 Sol (OpenAI, effort max) for the English translation; Claude Fable 5.2 and Claude Opus 5.5 for the glossary; Claude Opus 5.5 for the prompt, checks, fixes, completeness comparison, and English book',
    'GPT-6 Astra for raw research answers; Claude Fable 5.2 for their reviews',
    'GPT-6 Astra (OpenAI, ChatGPT Pro mode) for this reader build, apparatus, and audit',
]

def sha(data):return hashlib.sha256(data).hexdigest()

def main():
    chunks=(ROOT/'work/fr/repo/RIGHTS_NOTICE.md').read_text().split('---')
    rights={'EN':chunks[0].replace('# Rights notice','').strip(),'FR':chunks[1].strip()}
    files=[];privacy=[]
    for lang,names in B.NAMES.items():
        page2=[]
        for index,(name,form) in enumerate(zip(names,B.FORMS)):
            tex=ROOT/'output'/lang/(name+'.tex');pdf=tex.with_suffix('.pdf')
            text=tex.read_text();raw=pdf.read_bytes();pdf_hash=sha(raw)
            record=json.loads((RECORDS/'build'/(name+'.json')).read_text())
            assert record['compiled_without_errors'],name
            assert all(not record['passes'][-1][k] for k in ('errors','missing_glyphs','undefined','unsettled')),name
            assert record['source_tex_sha256']==sha(tex.read_bytes()),('stale source',name)
            assert record['pdf_sha256']==pdf_hash,('stale PDF',name)
            front=B.front(lang,form);missing=[token for token in COMMON if token not in front]
            assert front in text and rights[lang] in front and not missing,name
            assert not FORBIDDEN.search(text),name
            exact_translation='translated by GPT-6.1 Sol (OpenAI, effort max)' in front
            assert lang!='EN' or exact_translation,name
            proc=subprocess.run(['pdftotext','-enc','UTF-8',str(pdf),'-'],capture_output=True)
            assert proc.returncode==0,name
            fulltext=proc.stdout.decode('utf-8')
            hits,_=privacy_scan(fulltext,str(pdf.relative_to(ROOT)),component='PDF text')
            with fitz.open(stream=raw,filetype='pdf') as doc:
                assert len(doc)==record['pages'],name
                metadata=json.dumps(doc.metadata,ensure_ascii=False)
                meta_hits,_=privacy_scan(metadata,str(pdf.relative_to(ROOT)),component='PDF metadata')
                forbidden=len(FORBIDDEN.findall(fulltext))
                assert not hits and not meta_hits and not forbidden,name
                assert TITLES[lang][index] in doc[0].get_text(),name
                credit_text=doc[1].get_text()
                credit_pixels=doc[1].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False).samples
                check=dict(file=str(tex.relative_to(ROOT)),language=lang,form=form,
                           front_exactly_emitted=True,rights_paragraph_exact=True,
                           required_common_credits=True,missing_common_tokens=[],
                           ai_assisted_phrase_present=False,front_sha256=sha(front.encode()),
                           pdf_sha256=pdf_hash,credits_page_text_sha256=sha(credit_text.encode()),
                           credits_page_pixels_sha256=sha(credit_pixels),
                           correct_form_title_rendered=True)
                if lang=='EN':check['requested_translation_credit_exact']=exact_translation
                files.append(check);page2.append((check['credits_page_text_sha256'],check['credits_page_pixels_sha256']))
                privacy.append(dict(file=str(pdf.relative_to(ROOT)),pages=len(doc),bytes=len(raw),sha256=pdf_hash,
                                    compile_hash_matches=True,extraction_exit=proc.returncode,text_characters=len(fulltext),
                                    private_path_or_email_matches=len(hits),metadata_private_matches=len(meta_hits),
                                    ai_assisted_phrase_matches=forbidden))
            assert sha(pdf.read_bytes())==pdf_hash,('PDF changed during audit',name)
        assert len(set(page2))==1,('credits page differs across forms',lang)
        for check in files:
            if check['language']==lang:check['credits_page_identical_across_language_forms']=True
    report=dict(source_readme='repo/README.md, Credits section',source_rights_notice='repo/RIGHTS_NOTICE.md',
                rights_paragraph_sha256={k:sha(v.encode()) for k,v in rights.items()},
                all_six_exact_rights_paragraphs=True,all_six_common_credits_present=True,
                all_six_fronts_match_emitted_files=True,ai_assisted_phrase_present=False,
                credits_render_identically_within_each_language=True,role_audit=ROLES,files=files)
    (RECORDS/'PACKAGING_CREDITS_VALIDATION.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    (RECORDS/'PACKAGING_PDF_PRIVACY.json').write_text(json.dumps(privacy,ensure_ascii=False,indent=2)+'\n')
    print('PASS: six current build hashes; six exact rights/credit fronts; identical credit-page rendering per language; full PDF text and metadata privacy scans.')

if __name__=='__main__':main()
