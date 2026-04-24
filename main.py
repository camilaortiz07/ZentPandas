import pandas as pd

from carga import cargar_todos
from limpieza import {
    limpiar_usuarios,
    limpiar_categorias,
    limpiar_medios_pago
}

print("\n" + "=" * 60)
print("CARGA DE DATOS")
print("=" * 60)

datos_crudos = cargar_todos()

print("\n" + "=" * 60)
print("PASO 2: LIMPIEZA DE DATOS")
print("=" * 60)

df_usuarios    = limpiar_usuarios(datos_crudos['usuarios'])
df_categorias  = limpiar_categorias(datos_crudos['categorias'])
df_medios_pago = limpiar_medios_pago(datos_crudos['medios_pago'])



print("\n" + "=" * 60)
print("Guardando archivos limpios")
print("=" * 60)

df_usuarios.to_csv('data/processed/usuarios_limpiados.csv', index=False)
print("Guardado: data/processed/usuarios_limpiados.csv")

df_categorias.to_csv('data/processed/categorias_limpiadas.csv', index=False)
print("Guardado: data/processed/categorias_limpiadas.csv")

df_medios_pago.to_csv('data/processed/medios_pago_limpios.csv', index=False)
print("Guardado: data/processed/medios_pago_limpios.csv")