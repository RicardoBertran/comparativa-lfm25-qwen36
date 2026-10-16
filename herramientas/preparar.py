"""Crea muestras nuevas; nunca sobrescribe una ronda existente."""
from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parents[1]
dest=ROOT/'ejecuciones'
dest.mkdir(exist_ok=False)
for model in ('liquid','qwen'):
    base=dest/model
    (base/'01-gastos').mkdir(parents=True)
    shutil.copytree(ROOT/'pruebas/02-inventario/inicial',base/'02-inventario')
    shutil.copytree(ROOT/'pruebas/03-organizacion/inicial',base/'03-organizacion')
    for prueba in ('01-gastos','02-inventario','03-organizacion'):
        shutil.copyfile(ROOT/'pruebas'/prueba/'prompt.txt',base/prueba/'prompt.txt')
print('Copias preparadas en ejecuciones. Cada prueba incluye su prompt original.')
