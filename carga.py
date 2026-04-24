import pandas as pd

def cargar_csv(ruta):
    " Carga un archivo CSV en un DataFrame de Pandas. "

    df = pd.read_csv(ruta)
    print(f"[carga] CSV cargado: {ruta}  →  {df.shape[0]} filas, {df.shape[1]} columnas")
    return df

def cargar_json(ruta):
    " Carga un archivo JSON en un DataFrame de Pandas. "

    df = pd.read_json(ruta)
    print(f"[carga] JSON cargado: {ruta}  →  {df.shape[0]} filas, {df.shape[1]} columnas")
    return df

def cargar_todos(base='data/raw/'):
    print("\nCargando todos los archivos")
    datos = {
        'usuarios': cargar_csv(base + 'usuarios.csv'),}
    
    print("\nTodos los archivos cargados exitosamente.")
    for nombre, df in datos.items():
        print(f"  {nombre:15} →  {df.shape[0]} filas")

    return datos