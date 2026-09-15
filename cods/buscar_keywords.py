import pandas as pd
import re

def search_keywords_in_bib(bib_file, keywords):
    """
    Busca palabras clave en abstracts de archivo .bib
    
    Args:
        bib_file: ruta al archivo .bib
        keywords: lista de palabras clave a buscar
    
    Returns:
        DataFrame con clave de entrada como primera columna y palabras clave como columnas adicionales
    """
    
    with open(bib_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer cada entrada con su clave (@article {clave, ...})
    entries = re.finditer(r'@\w+\s*\{([^},]+),(.*?)(?=@\w+\s*\{|\Z)', content, re.DOTALL)
    
    results = []
    
    for match in entries:
        clave = match.group(1).strip()
        entry_content = match.group(2)
        
        # Extraer abstract
        abstract_match = re.search(r'abstract\s*=\s*["{]([^"}]+)["}]', entry_content, re.IGNORECASE | re.DOTALL)
        abstract = abstract_match.group(1).strip() if abstract_match else ""
        
        if not abstract:
            continue
        
        # Convertir a minúscula para búsqueda
        abstract_lower = abstract.lower()
        
        # Crear fila para esta entrada
        row = {'autor': clave}
        
        # Buscar cada palabra clave
        for keyword in keywords:
            keyword_lower = keyword.lower()
            count = abstract_lower.count(keyword_lower)
            row[keyword] = count
        
        results.append(row)
    
    # Crear DataFrame y rellenar con 0 en caso de valores faltantes
    df = pd.DataFrame(results)
    df = df.fillna(0).astype({col: int for col in keywords})
    
    # Filtrar: solo mantener autores que tengan al menos una palabra clave
    df = df[df[keywords].sum(axis=1) > 0]
    
    return df


# Uso
if __name__ == "__main__":
    # Definir palabras clave
    keywords = ["cyclone", "extratropical", "EOF"]
    
    # Buscar
    df = search_keywords_in_bib("bibliografia_vr1.bib", keywords)
    
    # Mostrar resultados con todas las columnas
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', None)
    print(df)