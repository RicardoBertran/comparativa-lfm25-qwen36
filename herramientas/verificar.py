"""Verifica integridad, tests originales y resultados guardados; no llama modelos."""
from pathlib import Path
import ast,hashlib,json,subprocess,sys
from auditar_organizacion import audit
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tests(p):
    tree=ast.parse(p.read_text(encoding='utf-8-sig'))
    return ast.dump(next(n for n in tree.body if isinstance(n,ast.ClassDef) and n.name=='TestsInventario'),include_attributes=False)
def verify():
    integrity=[]
    for name,h in json.loads((ROOT/'SHA256SUMS.json').read_text()).items():
        p=ROOT/name
        if not p.is_file() or sha(p)!=h:integrity.append(name)
    cases={};initial=ROOT/'pruebas/02-inventario/inicial/inventario.py'
    for name,rel in [('inicial','inicial'),('liquid','resultados/liquid'),('qwen','resultados/qwen')]:
        p=ROOT/'pruebas/02-inventario'/rel/'inventario.py'
        run=subprocess.run([sys.executable,'-B',str(p),'-v'],capture_output=True,text=True,cwd=ROOT)
        output=(run.stdout+run.stderr).replace(str(ROOT),'<REPOSITORIO>').replace(str(ROOT).replace('\\','/'),'<REPOSITORIO>')
        cases[name]={'codigo_salida':run.returncode,'tests_identicos':tests(p)==tests(initial),'salida':output}
    org={m:audit(ROOT/'pruebas/03-organizacion/resultados'/m) for m in ('liquid','qwen')}
    ok=not integrity and all(x['tests_identicos'] for x in cases.values()) and cases['inicial']['codigo_salida']==1 and all(cases[m]['codigo_salida']==0 for m in ('liquid','qwen')) and org['liquid']['clasificados_correctamente']==2 and not org['liquid']['entrada_conservada'] and org['qwen']['clasificados_correctamente']==10 and org['qwen']['entrada_conservada'] and not org['qwen']['errores']
    return {'verificacion_del_paquete_ok':ok,'fallos_integridad':integrity,'inventario':cases,'organizacion':org,'alcance':'Archivos y tests; sin nueva ejecución de agentes. La revisión parcial de gastos en navegador se documenta por separado en docs/revision-navegador.json.'}
if __name__=='__main__':
    report=verify();print(json.dumps(report,ensure_ascii=False,indent=2));raise SystemExit(not report['verificacion_del_paquete_ok'])
