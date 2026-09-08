#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Contador de palabras clave en archivos .TEX
Simple, eficiente y pensado para archivos planos LaTeX.
"""
import os
import sys
import re
from pathlib import Path
from collections import Counter

def extraer_citas(file, case_sensitive=False):
    patron = re.compile(r'\\cite[pt]\{([^}]*)\}')
    contador = Counter()
    total_citas = 0
    
    try:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            for linea in f:
                if not case_sensitive:
                    linea = linea.lower()
                    # El patrón también debe buscar en minúsculas
                    matches = re.finditer(r'\\cite[pt]\{([^}]*)\}', linea)
                else:
                    matches = patron.finditer(linea)
                
                for match in matches:
                    contenido = match.group(1)
                    # Separar por comas (múltiples autores en una cita)
                    autores = [a.strip() for a in contenido.split(',') if a.strip()]
                    for autor in autores:
                        contador[autor] += 1
                        total_citas += 1
    except (IOError, OSError) as e:
        print(f"⚠️  Error leyendo {file}: {e}")
        return
    
    # Mostrar resultados
    print(f"🔍 Archivo: {Path(file).name}")
    print(f"📄 Total de citas encontradas: {total_citas}")
    print(f"👤 Autores únicos: {len(contador)}")
    print("-" * 50)
    
    # Ordenar por frecuencia (mayor primero)
    for autor, veces in contador.most_common():
        print(f"  {veces:>4d}  →  {autor}")
    
    print("-" * 50)
    print(f"📊 TOTAL: {total_citas} citas de {len(contador)} autores distintos")
    
def contar_en_archivo(ruta_archivo, palabra, case_sensitive=False):
    """
    Cuenta ocurrencias de una palabra en un archivo .tex.
    Lee línea por línea para ser eficiente con archivos grandes.
    """
    contador = 0
    palabra_busqueda = palabra if case_sensitive else palabra.lower()
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8', errors='ignore') as f:
            for num_linea, linea in enumerate(f, start=1):
                linea_busqueda = linea if case_sensitive else linea.lower()
                # Contar ocurrencias en la línea
                ocurrencias = linea_busqueda.count(palabra_busqueda)
                if ocurrencias > 0:
                    contador += ocurrencias
    except (IOError, OSError) as e:
        print(f"  ⚠️  Error leyendo {ruta_archivo}: {e}")
        return 0
    
    return contador
def extraer_autores(file, case_sensitive=False):
    r"""Extrae autores de \citep{} y \citet{} como un set."""
    patron = r'\\cite[pt]\{([^}]*)\}'
    autores = set()
    
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        for linea in f:
            if not case_sensitive:
                linea = linea.lower()
            for match in re.finditer(patron, linea):
                contenido = match.group(1)
                for autor in contenido.split(','):
                    a = autor.strip()
                    if a:
                        autores.add(a)
    return autores


def cuenta(palabra,file,case_sensitive = False):
    archivos_tex = [Path(file)]
    if not archivos_tex:
        print(f"❌ No se encontraron archivos .tex en: {file}")
    else:
        print(f"🔍 Buscando: \"{palabra}\"")    
        print(f"📄 Archivos .tex encontrados: {len(archivos_tex)}")
        print(f"🔤 Case sensitive: {'Sí' if case_sensitive else 'No'}")
        print("-" * 50)
        
        total = 0
        resultados = []
        
        for archivo in archivos_tex:
            cuenta = contar_en_archivo(archivo, palabra, case_sensitive)
            if cuenta > 0:
                resultados.append((archivo, cuenta))
            total += cuenta
        
        # Mostrar resultados ordenados por cantidad (mayor primero)
        resultados.sort(key=lambda x: x[1], reverse=True)
        
        for archivo, cuenta in resultados:        
            ruta_relativa = archivo.name
            print(f"  {cuenta:>4d}  →  {ruta_relativa}")
        
        print("-" * 50)
        print(f"📊 TOTAL: {total} ocurrencias de \"{palabra}\"")
        
        sin_coincidencias = len(archivos_tex) - len(resultados)
        if sin_coincidencias > 0:
            print(f"   ({sin_coincidencias} archivos sin coincidencias)")

def comparar_citas(file_viejo, file_nuevo, case_sensitive=False):
    """Compara dos versiones y muestra solo los autores diferentes."""
    
    autores_viejo = extraer_autores(file_viejo, case_sensitive)
    autores_nuevo = extraer_autores(file_nuevo, case_sensitive)
    
    # Diferencias
    quitados = autores_viejo - autores_nuevo   # En viejo, no en nuevo
    agregados = autores_nuevo - autores_viejo   # En nuevo, no en viejo
    
    print(f"📄 Viejo: {Path(file_viejo).name}")
    print(f"📄 Nuevo: {Path(file_nuevo).name}")
    print("-" * 50)
    
    if quitados:
        print(f"➖ AUTORES ELIMINADOS ({len(quitados)}):")
        for a in sorted(quitados):
            print(f"     {a}")
    else:
        print("➖ No se eliminó ningún autor")
    
    print()
    
    if agregados:
        print(f"➕ AUTORES AGREGADOS ({len(agregados)}):")
        for a in sorted(agregados):
            print(f"     {a}")
    else:
        print("➕ No se agregó ningún autor")
    
    if not quitados and not agregados:
        print("✅ Ambos archivos tienen exactamente los mismos autores.")

def contar_autores(file, case_sensitive=False):
    r"""Cuenta autores de \citep{} y \citet{}."""
    patron = r'\\cite[pt]\{([^}]*)\}'
    contador = Counter()
    
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        for linea in f:
            if not case_sensitive:
                linea = linea.lower()
            for match in re.finditer(patron, linea):
                for autor in match.group(1).split(','):
                    a = autor.strip()
                    if a:
                        contador[a] += 1
    return contador


def comparar_citas_con_cantidad(file_viejo, file_nuevo, case_sensitive=False):
    """Compara dos versiones: autores diferentes Y cambios en cantidad."""
    
    viejo = contar_autores(file_viejo, case_sensitive)
    nuevo = contar_autores(file_nuevo, case_sensitive)
    
    todos = set(viejo.keys()) | set(nuevo.keys())
    
    print(f"📄 Viejo: {Path(file_viejo).name}")
    print(f"📄 Nuevo: {Path(file_nuevo).name}")
    print("-" * 50)
    
    hay_diferencias = False
    
    for autor in sorted(todos):
        c_viejo = viejo.get(autor, 0)
        c_nuevo = nuevo.get(autor, 0)
        
        if c_viejo != c_nuevo:
            hay_diferencias = True
            if c_viejo == 0:
                print(f"  ➕ {autor}: 0 → {c_nuevo}  (nuevo)")
            elif c_nuevo == 0:
                print(f"  ➖ {autor}: {c_viejo} → 0  (eliminado)")
            else:
                cambio = c_nuevo - c_viejo
                signo = "+" if cambio > 0 else ""
                print(f"  ✏️  {autor}: {c_viejo} → {c_nuevo}  ({signo}{cambio})")
    
    if not hay_diferencias:
        print("✅ Ambos archivos tienen exactamente los mismos autores y cantidades.")
    else:
        print("-" * 50)
        print(f"📊 Total citas viejo: {sum(viejo.values())}")
        print(f"📊 Total citas nuevo: {sum(nuevo.values())}")

def buscar_autor_en_archivos(lista_archivos, autor_buscado, case_sensitive=False):
    r"""
    Busca una referencia de autor exacta en múltiples archivos .tex.
    Busca en \citep{} y \citet{}.
    
    Args:
        lista_archivos: Lista de rutas a archivos .tex
        autor_buscado: Nombre de la referencia (ej: 'gentile2025response')
        case_sensitive: Si debe diferenciar mayúsculas/minúsculas
    
    Returns:
        Dict con resultados de búsqueda
    """
    patron = r'\\cite[pt]\{([^}]*)\}'
    resultados = {}
    
    autor_busqueda = autor_buscado if case_sensitive else autor_buscado.lower()
    
    for archivo in lista_archivos:
        archivo_path = Path(archivo)
        
        if not archivo_path.exists():
            print(f"⚠️  Archivo no encontrado: {archivo}")
            continue
        
        contador_archivo = 0
        ocurrencias = []
        
        try:
            with open(archivo_path, 'r', encoding='utf-8', errors='ignore') as f:
                for num_linea, linea in enumerate(f, start=1):
                    
                    for match in re.finditer(patron, linea):
                        contenido = match.group(1)
                        
                        autores = [a.strip() for a in contenido.split(',')]
                        
                        for autor in autores:
                            autor_comparar = autor if case_sensitive else autor.lower()
                            
                            if autor_busqueda == autor_comparar:
                                contador_archivo += 1
                                ocurrencias.append({
                                    'linea': num_linea,
                                    'cita_completa': f'\\cite{match.group(0)[5:]}'
                                })
        
        except (IOError, OSError) as e:
            print(f"⚠️  Error leyendo {archivo_path.name}: {e}")
            continue
        
        if contador_archivo > 0:
            resultados[archivo_path.name] = {
                'count': contador_archivo,
                'ocurrencias': ocurrencias
            }
    
    # Mostrar resultados
    print(f"🔍 Buscando: \"{autor_buscado}\"")
    print(f"📂 Archivos analizados: {len(lista_archivos)}")
    print(f"🔤 Case sensitive: {'Sí' if case_sensitive else 'No'}")
    print("-" * 60)
    
    if resultados:
        total_ocurrencias = sum(r['count'] for r in resultados.values())
        print(f"✅ Encontrado en {len(resultados)} archivo(s)\n")
        
        for archivo, datos in sorted(resultados.items(), key=lambda x: x[1]['count'], reverse=True):
            print(f"  📄 {archivo}")
            for ocurr in datos['ocurrencias']:
                print(f"     → Línea {ocurr['linea']}: {ocurr['cita_completa']}")
            print(f"     📊 Total: {datos['count']}")
        
        print("-" * 60)
        print(f"📊 TOTAL: {total_ocurrencias} ocurrencias en {len(resultados)} archivo(s)")
    else:
        print(f"❌ Referencia \"{autor_buscado}\" no encontrada en ningún archivo.")
    
    print()
    return resultados