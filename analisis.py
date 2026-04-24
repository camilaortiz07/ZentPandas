import pandas as pd
def analizar_frecuencia_categoria(gastos_completos):
    """
    1. ANÁLISIS DE FRECUENCIA: El "Vicio" más constante
    
    Detecta cuál es la categoría de gasto que más veces repites.
    No importa cuánto gastes cada vez, sino cuántas veces sacas la billetera.
    Pregunta: ¿Cuál es la categoría donde realizas compras con mayor frecuencia?
    """
    print("\n" + "=" * 70)
    print("1. ANÁLISIS DE FRECUENCIA: El 'Vicio' más constante")
    print("=" * 70)
    print("¿Cuál es la categoría donde realizas compras con mayor frecuencia?")
    
    frecuencia_categorias = gastos_completos['nombre_categoria'].value_counts()
    print("\nFrecuencia de compras por categoría:")
    print(frecuencia_categorias.to_string())
    
    if len(frecuencia_categorias) > 0:
        categoria_mas_frecuente = frecuencia_categorias.index[0]
        veces = frecuencia_categorias.iloc[0]
        print(f"\n→ RESULTADO: '{categoria_mas_frecuente}' es tu 'vicio' más constante")
        print(f"  Has comprado en esta categoría {veces} veces")
    
    return frecuencia_categorias


def analizar_frecuencia_comercio(gastos_completos):
    """
    Análisis de frecuencia por comercio específico.
    
    Pregunta: ¿Cuál es el comercio donde realizas compras con mayor frecuencia?
    """
    print("\n" + "=" * 70)
    print("ANÁLISIS COMPLEMENTARIO: Frecuencia por Comercio")
    print("=" * 70)
    
    frecuencia_comercios = gastos_completos['comercio_id'].value_counts()
    print("\nFrecuencia de compras por comercio (Top 10):")
    print(frecuencia_comercios.head(10).to_string())
    
    return frecuencia_comercios


def analizar_agregacion_dinero(gastos_completos):
    """
    2. ANÁLISIS DE AGREGACIÓN: El "Pozo Negro" de dinero
    
    Suma el dinero real acumulado por cada categoría.
    Agrupa todos los pequeños gastos y muestra el golpe total a tu bolsillo.
    
    Pregunta: ¿Cuál es el monto total acumulado por cada categoría de gasto?
    """
    print("\n" + "=" * 70)
    print("2. ANÁLISIS DE AGREGACIÓN: El 'Pozo Negro' de dinero")
    print("=" * 70)
    print("¿Cuál es el monto total acumulado por cada categoría?")
    
    gasto_total_por_categoria = (
        gastos_completos
        .groupby('nombre_categoria')['monto']
        .sum()
        .sort_values(ascending=False)
    )
    
    print("\nDinero acumulado por categoría:")
    for categoria, total in gasto_total_por_categoria.items():
        print(f"  {categoria:25} → ${total:>12,.0f}")
    
    total_general = gasto_total_por_categoria.sum()
    print(f"\n  {'TOTAL':25} → ${total_general:>12,.0f}")
    
    return gasto_total_por_categoria


def analizar_alerta_roja(df_gastos, limite_gasto_hormiga=20000):
    """
    3. ANÁLISIS CON FILTRADO Y CONTEO: La "Alerta Roja"
    
    Args:
        df_gastos: DataFrame de gastos
        limite_gasto_hormiga: Monto en pesos. Gastos superiores a este se consideran "alertas rojas"
    """
    print("\n" + "=" * 70)
    print("3. ANÁLISIS CON FILTRADO Y CONTEO: La 'Alerta Roja'")
    print("=" * 70)
    print(f"¿Cuántos gastos superan el límite de ${limite_gasto_hormiga:,} (gasto hormiga)?")
    
    # Filtrar gastos por encima del límite
    gastos_alerta = df_gastos[df_gastos['monto'] > limite_gasto_hormiga]
    total_alertas = len(gastos_alerta)
    monto_total_alertas = gastos_alerta['monto'].sum()
    promedio_alerta = gastos_alerta['monto'].mean()
    
    print(f"\n→ RESULTADO ALERTA ROJA:")
    print(f"  Gastos que superan ${limite_gasto_hormiga:,}: {total_alertas}")
    print(f"  Monto total en alertas rojas: ${monto_total_alertas:,.0f}")
    print(f"  Promedio por alerta: ${promedio_alerta:,.0f}")
    
    if total_alertas > 0:
        print(f"\n  Distribución de alertas rojas:")
        for _, gasto in gastos_alerta.iterrows():
            estado_icon = "✓" if gasto['estado'] == 'aprobado' else "✗"
            print(f"    {estado_icon} ID {gasto['gasto_id']}: ${gasto['monto']:>10,.0f} - {gasto['descripcion']}")
    
    return gastos_alerta


def ejecutar_todos_analisis(df_usuarios, df_gastos, gastos_completos, gastos_con_medio):
    """
    Ejecuta todos los análisis a la vez.
    Combina los tres análisis principales del proyecto.
    """
    # Análisis de frecuencia
    analizar_frecuencia_categoria(gastos_completos)
    analizar_frecuencia_comercio(gastos_completos)
    
    # Análisis de agregación
    analizar_agregacion_dinero(gastos_completos)
    
    # Análisis de alerta roja (con límite de $20.000)
    analizar_alerta_roja(df_gastos, limite_gasto_hormiga=20000)
    
    # Análisis adicionales del sistema anterior
    print("\n" + "=" * 70)
    print("ANÁLISIS ADICIONALES")
    print("=" * 70)
    
    # Medio de pago más usado
    print("\n--- Medio de pago más utilizado ---")
    medio_mas_usado = gastos_con_medio['nombre_medio'].value_counts()
    print(medio_mas_usado.to_string())
    
    # Usuarios por ciudad
    print("\n--- Usuarios por ciudad ---")
    usuarios_por_ciudad = df_usuarios['ciudad'].value_counts()
    print(usuarios_por_ciudad.to_string())
    
    # Gasto promedio por usuario
    print("\n--- Gasto promedio por usuario ---")
    gasto_promedio = (
        df_gastos
        .groupby('usuario_id')['monto']
        .mean()
        .sort_values(ascending=False)
    )
    print(f"Promedio general: ${gasto_promedio.mean():,.0f}")
    print(f"Usuario con mayor gasto promedio: ID {gasto_promedio.idxmax()} (${gasto_promedio.max():,.0f})")
    
    # Estado de los gastos
    print("\n--- Estado de los gastos ---")
    total = len(df_gastos)
    por_estado = df_gastos['estado'].value_counts()
    for estado, cantidad in por_estado.items():
        porcentaje = (cantidad / total) * 100
        print(f"  {estado:12}: {cantidad} gastos  ({porcentaje:.1f}%)")

