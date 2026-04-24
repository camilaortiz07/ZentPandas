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
        mediana_edad = df['edad'].median()
        df['edad'] = df['edad'].fillna(mediana_edad)

        ##Eliminar Duplicados
        antes = len(df)
        df = df.drop_duplicates()
        print(f"Filas Eliminadas por Duplicados: {antes - len(df)}")

        #3Limpieza especifica
        correccion_ciudades = {
            'bogotá': 'bogota',
            'bógota': 'bogota',
            'bogóta': 'bogota',
            'bogota': 'bogota',
            'medellín': 'medellin',
            'medelln': 'medellin',
            'medelín': 'medellin',
            'cartenagena': 'cartagena',
            'baranquilla': 'barranquilla',
            'bucaramnga': 'bucaramanga',
            'desconocida': 'medellin',  # valor por defecto
         }
        df['ciudad'] = df['ciudad'].replace(correccion_ciudades)
        print("Ciudades después de limpiar:")
        print(df['ciudad'].value_counts())

        correccion_genero = {
            'masculino': 'm',
            'male': 'm',
            'femenino': 'f',
            'female': 'f',
            'desconocido': 'm',  # valor por defecto
        }
        df['genero'] = df['genero'].replace(correccion_genero)
        print("Géneros después de limpiar:")
        print(df['genero'].value_counts())  
        
        # convertir todas las columnas id a int64 para evitar .0
        id_columns = [col for col in df.columns if 'id' in col.endswitch('id')]
        for col in id_columns:
            df[col] = df[col].astype('Int64')

        return df