"""Empaqueta exclusivamente los fuentes necesarios del informe LaTeX vigente."""
from pathlib import Path
import zipfile

ROOT=Path(__file__).resolve().parents[1]
REPORT=ROOT/'informe'
FILES=['main.tex','referencias.bib','acmart.cls','ACM-Reference-Format.bst',
       'figuras/comparacion.pdf','figuras/aprendizaje.pdf']
FILES += [p.relative_to(REPORT).as_posix() for p in sorted((REPORT/'secciones').glob('*.tex'))]

if __name__=='__main__':
    for name in FILES:
        if not (REPORT/name).is_file():
            raise FileNotFoundError(name)
    output=ROOT/'grupo5_overleaf.zip'
    with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
        for name in FILES:
            archive.write(REPORT/name,name)
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(FILES)
    print(output)
