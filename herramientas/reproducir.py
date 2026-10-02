"""Repite el protocolo en un directorio nuevo, conservando los resultados originales."""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destino',required=True)
    args=parser.parse_args()
    destination=Path(args.destino).resolve()
    if destination.exists():
        raise FileExistsError('Use una carpeta nueva para conservar la evidencia previa')
    destination.mkdir(parents=True)
    for directory in ('codigo','herramientas'):
        shutil.copytree(ROOT/directory,destination/directory,ignore=shutil.ignore_patterns('__pycache__'))
    (destination/'investigacion').mkdir()
    (destination/'informe').mkdir()
    shutil.copy2(ROOT/'requirements-lock.txt',destination/'requirements-lock.txt')
    sources=ROOT/'datos/originales'
    if len(list(sources.glob('*.conllu')))==3:
        shutil.copytree(sources,destination/'datos/originales')
    else:
        subprocess.run([sys.executable,'herramientas/descargar_recursos.py'],cwd=destination,check=True)
    commands=[['codigo/pln.py','preparar'],['-m','unittest','discover','-s','codigo','-p','test_*.py','-v'],
              ['codigo/experimentos.py'],['codigo/pln.py','evaluar'],['codigo/analizar.py']]
    for command in commands:
        subprocess.run([sys.executable,*command],cwd=destination,check=True)
    print('Replica conservada en:',destination)

if __name__=='__main__': main()
