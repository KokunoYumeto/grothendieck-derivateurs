from pathlib import Path
import urllib.request,json,re,concurrent.futures
root=Path(__file__).resolve().parents[1];dest=root/'work/sources'
urls={
'Isbell1974_annals':'https://annals.math.princeton.edu/1974/100-3/p05',
'AdamekReiterman1975_doi':'https://doi.org/10.1090/S0002-9947-1975-0376799-X',
'Husainov2002_RG':'https://www.researchgate.net/publication/232724279_Homological_dimension_theory_of_small_categories',
'Oberst1968_gdz_search':'https://gdz.sub.uni-goettingen.de/search?query=Homology%20of%20categories%20and%20exactness%20of%20direct%20limits',
}
def fetch(it):
    name,url=it;r={'name':name,'url':url}
    try:
        response=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=30)
        d=response.read();s=d.decode('utf8',errors='replace');(dest/(name+'.html')).write_text(s)
        r.update(url=response.url,bytes=len(d),links=[x for x in re.findall(r'(?:href|content)=[\"\']([^\"\']+)',s) if 'pdf' in x.lower() or 'download' in x.lower() or 'BF011' in x])
    except Exception as e:r['error']=type(e).__name__+': '+str(e)
    return r
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e:results=list(e.map(fetch,urls.items()))
out=json.dumps(results,indent=2);(root/'code/literature_fetch_more.out').write_text(out+'\n');print(out)
