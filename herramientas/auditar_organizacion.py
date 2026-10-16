"""Auditor de solo lectura para la muestra ficticia de 12 archivos."""
from pathlib import Path
import csv,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
EXPECTED={'apuntes_07.txt':'facturas','registro_B.md':'facturas','resumen_azul.csv':'facturas','borrador_12.md':'documentos','datos_04.json':'documentos','factura_pendiente.txt':'documentos','nota_final.log':'documentos','documento_09.txt':'notas','factura_ideas.log':'notas','lista_11.csv':'notas'}
COLS=['archivo_original','categoria','archivo_destino','duplicado_de','estado']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def audit(base):
    base=Path(base);initial=ROOT/'pruebas/03-organizacion/inicial/entrada'
    refs={p.name:sha(p) for p in initial.iterdir() if p.is_file()}
    groups={}
    for name,h in refs.items():groups.setdefault(h,[]).append(name)
    cat={refs[n]:c for n,c in EXPECTED.items()}
    result=base/'resultado'; errors=[];details=[]
    files=sorted(p for p in result.rglob('*') if p.is_file() and p!=result/'informe.csv')
    by_hash={}
    for p in files:by_hash.setdefault(sha(p),[]).append(p)
    for h,names in groups.items():
        outputs=by_hash.get(h,[])
        correct=len(outputs)==1 and outputs[0].parent==result/cat[h]
        details.append({'originales':names,'esperada':cat[h],'destinos':[p.relative_to(result).as_posix() for p in outputs],'correcto':correct})
        if not correct:errors.append('Clasificación o número de copias incorrecto: '+names[0])
    if set(by_hash)!=set(groups):errors.append('Contenidos de salida ajenos o faltantes')
    entry=base/'entrada'
    actual={p.relative_to(entry).as_posix():sha(p) for p in entry.rglob('*') if p.is_file()} if entry.exists() else {}
    preserved=actual==refs
    if not preserved:errors.append('La entrada no conserva exactamente los 12 originales')
    rows=[];encoding='desconocida'
    try:
        raw=(result/'informe.csv').read_bytes()
        encoding='utf-16' if raw.startswith((b'\xff\xfe',b'\xfe\xff')) else 'utf-8-sig'
        reader=csv.DictReader(raw.decode(encoding).splitlines());rows=list(reader)
        if reader.fieldnames!=COLS:errors.append('Columnas CSV distintas a las solicitadas')
        if len(rows)!=12 or sorted(r.get('archivo_original','') for r in rows)!=sorted(refs):errors.append('CSV sin una fila exacta por original')
        for r in rows:
            n=r.get('archivo_original','')
            if n not in refs:continue
            h=refs[n];dest=r.get('archivo_destino','');dup=r.get('duplicado_de','')
            if r.get('categoria')!=cat[h]:errors.append('Categoría CSV incorrecta: '+n)
            state=r.get('estado','').upper()
            discarded='DESCARTADO' in state
            if discarded:
                if dup not in refs or dup==n or refs.get(dup)!=h:errors.append('duplicado_de no identifica original equivalente: '+n)
                elif not any(x.get('archivo_original')==dup and 'DESCARTADO' not in x.get('estado','').upper() for x in rows):errors.append('duplicado_de no referencia una fila conservada: '+n)
                if dest:errors.append('Destino declarado para archivo descartado: '+n)
            else:
                if state not in ('UNICO','CONSERVADO'):errors.append('Estado no reconocido: '+n)
                if dup not in ('','No'):errors.append('Marca de duplicado contradictoria: '+n)
                parts=Path(dest)
                target=result/parts
                if not dest or parts.is_absolute() or '..' in parts.parts or not target.is_file() or sha(target)!=h:errors.append('Destino conservado inexistente o distinto: '+n)
                elif target.parent!=result/cat[h]:errors.append('Destino CSV en categoría incorrecta: '+n)
        if sum('DESCARTADO' in r.get('estado','').upper() for r in rows)!=2:errors.append('CSV no declara dos descartes')
    except (OSError,UnicodeError,csv.Error) as e:errors.append('CSV ilegible: '+type(e).__name__)
    return {'clasificados_correctamente':sum(x['correcto'] for x in details),'contenidos_unicos_esperados':10,'archivos_salida':len(files),'contenidos_salida_preservados':set(by_hash)==set(groups),'entrada_conservada':preserved,'archivos_entrada':len(actual),'filas_csv':len(rows),'codificacion_csv':encoding,'detalle':details,'errores':errors}
if __name__=='__main__':
    if len(sys.argv)!=2:raise SystemExit('Uso: python herramientas/auditar_organizacion.py RUTA_DE_LA_PRUEBA')
    report=audit(sys.argv[1]);print(json.dumps(report,ensure_ascii=False,indent=2));raise SystemExit(bool(report['errores']))
