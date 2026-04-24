import pandas as pd

from carga import cargar_todos
from limpieza import (
    limpiar_comercios,
    limpiar_gastos,
    limpiar_usuarios,
    limpiar_categorias,
    limpiar_medios_pago
)
from union import (
    hacer_gastos_completos,
    hacer_gastos_con_medios_pago,
    hacer_gastos_con_usuarios,
)
from analisis import ejecutar_todos_analisis

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
df_comercios   = limpiar_comercios(datos_crudos['comercios'])
df_gastos      = limpiar_gastos(datos_crudos['gastos'])



print("\n" + "=" * 60)
print("GUARDADO DE DATOS LIMPIOS")
print("=" * 60)

df_usuarios.to_csv('data/processed/usuarios_limpiados.csv', index=False)
print("Guardado: data/processed/usuarios_limpiados.csv")

df_categorias.to_csv('data/processed/categorias_limpiadas.csv', index=False)
print("Guardado: data/processed/categorias_limpiadas.csv")

df_medios_pago.to_csv('data/processed/medios_pago_limpios.csv', index=False)
print("Guardado: data/processed/medios_pago_limpios.csv")

df_comercios.to_csv('data/processed/comercios_limpios.csv', index=False)
print("Guardado: data/processed/comercios_limpios.csv")

df_gastos.to_csv('data/processed/gastos_limpios.csv', index=False)
print("Guardado: data/processed/gastos_limpios.csv")

#Unión de datos para análisis
print("\n" + "=" * 60)
print("PASO 4: UNIONES DE DATOS")
print("=" * 60)

# Hacer los merges usando las funciones de union.py
gastos_completos = hacer_gastos_completos(df_gastos, df_comercios, df_categorias)
gastos_completos.to_csv('data/processed/gastos_completos.csv', index=False)
print("Guardado: data/processed/gastos_completos.csv")

gastos_con_medio = hacer_gastos_con_medios_pago(df_gastos, df_medios_pago)
gastos_con_medio.to_csv('data/processed/gastos_con_medios_pago.csv', index=False)
print("Guardado: data/processed/gastos_con_medios_pago.csv")

gastos_con_usuario = hacer_gastos_con_usuarios(df_gastos, df_usuarios)
gastos_con_usuario.to_csv('data/processed/gastos_con_usuarios.csv', index=False)
print("Guardado: data/processed/gastos_con_usuarios.csv")

print("\n" + "=" * 60)
print("PASO 5: ANÁLISIS DE DATOS")
print("=" * 60)

# Ejecutar todos los análisis usando las funciones de analisis.py
ejecutar_todos_analisis(df_usuarios, df_gastos, gastos_completos, gastos_con_medio)

print("\n" + "=" * 60)
print("Análisis finalizado.")
print("=" * 60)