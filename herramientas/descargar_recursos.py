"""Descarga recursos abiertos sin autenticación y registra SHA-256 y URL final.

No publica los PDF bibliográficos. Son copias locales de consulta del grupo.
"""
from pathlib import Path
import concurrent.futures
import hashlib
import json
import urllib.request
try:
    import truststore
    truststore.inject_into_ssl()
except ImportError:
    pass

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = {
    'investigacion/pdf/hochreiter1997.pdf': 'https://www.bioinf.jku.at/publications/older/2604.pdf',
    'investigacion/pdf/greff2017.pdf': 'https://arxiv.org/pdf/1503.04069',
    'investigacion/pdf/sherstinsky2020.pdf': 'https://arxiv.org/pdf/1808.03314',
    'investigacion/pdf/pascanu2013.pdf': 'https://proceedings.mlr.press/v28/pascanu13.pdf',
    'investigacion/pdf/bengio2003.pdf': 'https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf',
    'investigacion/pdf/mikolov2010.pdf': 'https://www.isca-archive.org/interspeech_2010/mikolov10_interspeech.pdf',
    'investigacion/pdf/sundermeyer2012.pdf': 'https://www.isca-archive.org/interspeech_2012/sundermeyer12_interspeech.pdf',
    'investigacion/pdf/srivastava2014.pdf': 'https://www.jmlr.org/papers/volume15/srivastava14a/srivastava14a.pdf',
    'investigacion/pdf/taule2008.pdf': 'https://aclanthology.org/L08-1222.pdf',
    'investigacion/pdf/doval2016.pdf': 'https://www.redalyc.org/pdf/5157/515754424008.pdf',
    'investigacion/pdf/bengio1994.pdf': 'https://www.cs.cmu.edu/~bhiksha/courses/deeplearning/Fall.2016/pdfs/Bengio_94.pdf',
    'investigacion/pdf/nivre2020.pdf': 'https://aclanthology.org/2020.lrec-1.497.pdf',
}
for split in ('train', 'dev', 'test'):
    name = f'es_ancora-ud-{split}.conllu'
    RESOURCES[f'datos/originales/{name}'] = f'https://raw.githubusercontent.com/UniversalDependencies/UD_Spanish-AnCora/r2.17/{name}'
for name in ('README.md', 'LICENSE.txt'):
    RESOURCES[f'datos/originales/{name}'] = f'https://raw.githubusercontent.com/UniversalDependencies/UD_Spanish-AnCora/r2.17/{name}'

def download(item):
    relative, url = item
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    result = {'archivo': relative, 'url': url}
    try:
        if path.exists():
            data = path.read_bytes()
            result.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), acceso='copia local de descarga previa', status=200)
            return result
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 Academic verification'})
        with urllib.request.urlopen(request, timeout=90) as response:
            data = response.read()
            result.update(status=response.status, url_final=response.url,
                          tipo=response.headers.get('Content-Type'))
        if path.suffix == '.pdf' and not data.startswith(b'%PDF'):
            raise ValueError('La respuesta no es un PDF')
        path.write_bytes(data)
        result.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), acceso='sin cuenta ni pago')
    except Exception as exc:
        result['error'] = str(exc)
    print(json.dumps(result, ensure_ascii=True), flush=True)
    return result

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(download, RESOURCES.items()))
    (ROOT / 'investigacion/acceso_verificado.json').write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    if any('error' in result for result in results):
        raise SystemExit('Hay descargas fallidas; revise el registro antes de preparar datos')
