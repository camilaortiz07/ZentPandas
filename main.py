import pandas as pd

from carga import cargar_todos
from limpieza import {
    limpiar_usuarios
}

print("\n" + "=" * 60)
print("CARGA DE DATOS")
print("=" * 60)

datos_crudos = cargar_todos()

print("\n" + "=" * 60)
print("PASO 2: LIMPIEZA DE DATOS")
print("=" * 60)

df_usuarios    = limpiar_usuarios(datos_crudos['usuarios'])