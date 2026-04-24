import pandas as pd

## Funciones Generales para cualquier DataFrame

def manejar_nulos(df, columnas_criticas = None):
    " Dectecta valores nulos en el DataFrame y los maneja según las columnas críticas. "

    print("\n Valores Nulos por Columna:")
    print(df.isnull().sum())

    if columnas_criticas:
        antes =len(df)
        df = df.dropna(subset=columnas_criticas)
        despues = len(df)
        print(f"Filas Elimindas por Nulos en {columnas_criticas}: {antes - despues}")

    return df

def estandarizar_texto(df, columnas):
    " Estandariza el texto en las columnas especificadas a minúsculas. "

    for col in columnas:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower()
    print(f"\n Columnas Estandarizadas: {columnas}")
    return df

def limpiar_ciudades(df, columna='ciudad'):
    """
    Limpia y estandariza nombres de ciudades.
    Corrige tildes, espacios y variaciones comunes.
    """
    correccion_ciudades = {
        # Bogotá
        'bogotá': 'bogota',
        'bógota': 'bogota',
        'bogóta': 'bogota',
        'bogota': 'bogota',
        # Medellín
        'medellín': 'medellin',
        'medelln': 'medellin',
        'medelín': 'medellin',
        'medelin': 'medellin',
        'medellin': 'medellin',
        # Cartagena
        'cartenagena': 'cartagena',
        'cartagena': 'cartagena',
        # Barranquilla
        'baranquilla': 'barranquilla',
        'barranquilla': 'barranquilla',
        'barraquilla': 'barranquilla',
        # Bucaramanga
        'bucaramnga': 'bucaramanga',
        'bucaramanga': 'bucaramanga',
        'bucarmanga': 'bucaramanga',
        # Cali
        'cali': 'cali',
        # Pereira
        'pereira': 'pereira',
        # Manizales
        'manizales': 'manizales',
        # Valores por defecto
        'sin_ciudad': 'medellin',
        '': 'medellin',
    }
    
    if columna in df.columns:
        df[columna] = df[columna].replace(correccion_ciudades)
        print(f"Ciudades después de limpiar:")
        print(df[columna].value_counts())
    
    return df

## Limpieza Especifica para cada archivo
def  limpiar_usuarios(df):

    print("\n Limpiando Usuarios")
    df = estandarizar_texto(df, ['usuario', 'nombre','apellido','email','ciudad','genero'])

    ##convertir datos a tipos adecuados
    df['edad'] = pd.to_numeric(df['edad'], errors='coerce').astype('Int64')
    df['fecha_registro'] = pd.to_datetime(df['fecha_registro'], errors='coerce')

    ## Manejar Nulos
    df = manejar_nulos(df, columnas_criticas=['usuario'])
    df['nombre'] = df['nombre'].fillna('anonimo')
    df['apellido'] = df['apellido'].fillna('desconocido')
    df['email'] = df['email'].fillna('sin_email')
    df['ciudad'] = df['ciudad'].fillna('sin_ciudad')
    df['genero'] = df['genero'].fillna('sin_genero')
    df['fecha_registro'] = df['fecha_registro'].fillna(pd.Timestamp('1900-01-01'))
    mediana_edad = round(df['edad'].median())
    df['edad'] = df['edad'].fillna(mediana_edad)

    ##Eliminar Duplicados
    antes = len(df)
    df = df.drop_duplicates()
    print(f"Filas Eliminadas por Duplicados: {antes - len(df)}")

    #Limpieza especifica
    df = limpiar_ciudades(df, columna='ciudad')

    correccion_genero = {
        'masculino': 'm',
        'male': 'm',
        'femenino': 'f',
        'female': 'f',
        'sin_genero': 'm',  # valor por defecto
        }
    df['genero'] = df['genero'].replace(correccion_genero)
    print("Géneros después de limpiar:")
    print(df['genero'].value_counts())  
        
    # convertir todas las columnas id a int64 para evitar .0
    id_columns = [col for col in df.columns if col.endswith('_id')]
    for col in id_columns:
        df[col] = df[col].astype('Int64')

    return df

#(símbolo de moneda o texto podría aparecer → lo removemos)    
def limpiar_categorias(df):
    print("\n Limpieza de categoria")
    df = estandarizar_texto(df, ['categoria_id','nombre_categoria'])
    df = manejar_nulos(df, columnas_criticas=['categoria_id','nombre_categoria'])

    df['limite_mensual'] = (
    df['limite_mensual']
    .astype(str)
    .str.replace('$', '', regex=False)   # quitar símbolo $
    .str.replace(',', '', regex=False)   # quitar comas de miles
    .str.strip()
    )
    df['limite_mensual'] = pd.to_numeric(df['limite_mensual'], errors='coerce')
    print("Límites mensuales (primeras filas):")
    print(df[['nombre_categoria', 'limite_mensual']].head())

    print(f"Filas finales en categorias: {len(df)}")

    id_columns = [col for col in df.columns if col.endswith('_id')]
    for col in id_columns:
        df[col] = df[col].astype('Int64')
    
    return df

def limpiar_medios_pago(df):
    print("\n Limpieza de medios de pago")
    df = estandarizar_texto(df, ['nombre_medio','tipo','banco'])
    df = manejar_nulos(df, columnas_criticas=['medio_id','nombre_medio'])
    df['banco'] = df['banco'].fillna('sin_banco')

    print(f"Filas finales en medios de pago: {len(df)}")

    id_columns = [col for col in df.columns if col.endswith('_id')]
    for col in id_columns:
        df[col] = df[col].astype('Int64')
    
    return df

def limpiar_comercios(df):
    print("\n Limpieza de comercios")
    df = estandarizar_texto(df, ['nombre','ciudad'])
    df = manejar_nulos(df, columnas_criticas=['comercio_id','nombre'])
    df['telefono'] = df['telefono'].fillna('sin_telefono')
    df['ciudad'] = df['ciudad'].fillna('sin_ciudad')

    ##Limpieza especifica de ciudades
    df = limpiar_ciudades(df, columna='ciudad')

    # JSON puede traer true/false como string en algunos casos
    df['activo'] = df['activo'].astype(bool)
    print("Comercios activos vs inactivos:")
    print(df['activo'].value_counts())

    print(f"Filas finales en comercios: {len(df)}")

    id_columns = [col for col in df.columns if col.endswith('_id')]
    for col in id_columns:
        df[col] = df[col].astype('Int64')
    
    return df

def limpiar_gastos(df):
    print("\n Limpieza de gastos")
    df = estandarizar_texto(df, ['descripcion', 'estado'])
    df = manejar_nulos(df, columnas_criticas=['gasto_id','usuario_id','monto'])
    df['descripcion'] = df['descripcion'].fillna('sin_descripcion')
    df['estado'] = df['estado'].fillna('Pendiente')

    #Corregir tipos de datos
    df['monto'] = pd.to_numeric(df['monto'], errors='coerce')

    #Corregir fechas con múltiples formatos
    #Algunos registros pueden tener formatos como: YYYYMMDD, YYYY/MM/DD, etc
    df['fecha'] = df['fecha'].astype(str).str.replace('/', '-', regex=False)  # convertir / a -
    #Ahora convierte YYYYMMDD a YYYY-MM-DD
    mask_yyyymmdd = df['fecha'].str.match(r'^\d{8}$')
    df.loc[mask_yyyymmdd, 'fecha'] = df.loc[mask_yyyymmdd, 'fecha'].str.replace(
        r'(\d{4})(\d{2})(\d{2})', r'\1-\2-\3', regex=True
    )
    df['fecha'] = pd.to_datetime(df['fecha'], errors='coerce')

    #Eliminar filas con fechas inválidas
    antes = len(df)
    df = df.dropna(subset=['fecha'])
    if antes - len(df) > 0:
        print(f"Filas con fechas inválidas eliminadas: {antes - len(df)}")

    #Limpieza específica: MONTOS NEGATIVOS
    #Un gasto no puede ser negativo. Los eliminamos.
    antes = len(df)
    df = df[df['monto'] > 0]
    print(f"Filas con monto negativo o cero eliminadas: {antes - len(df)}")

     #Estandarizar el campo ESTADO
    estados_validos = ['aprobado', 'rechazado', 'pendiente']
    invalidos = ~df['estado'].isin(estados_validos)
    if len(df[invalidos]) > 0:
        print(f"Estados inválidos encontrados: {df[invalidos]['estado'].unique()}")
        # Los que no están en la lista → 'pendiente' como valor por defecto
        df.loc[invalidos, 'estado'] = 'pendiente'
    print("Estados después de limpiar:")
    print(df['estado'].value_counts())

    print(f"Filas finales en gastos: {len(df)}")
    
    id_columns = [col for col in df.columns if col.endswith('_id')]
    for col in id_columns:
        df[col] = df[col].astype('Int64')
    
    return df