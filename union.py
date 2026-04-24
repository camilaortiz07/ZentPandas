import pandas as pd

def hacer_gastos_completos(df_gastos, df_comercios, df_categorias):
    print("\n Uniendo gastos con comercios y categorias")
    gastos_comercios = df_gastos.merge(
        df_comercios[['comercio_id', 'categoria_id', 'nombre']],
        on='comercio_id',
        how='left',
    )

    gastos_completos = gastos_comercios.merge(
        df_categorias[['categoria_id', 'nombre_categoria']],
        on='categoria_id',
        how='left',
    )

    print(f"Filas en gastos_completos: {len(gastos_completos)}")
    return gastos_completos

def hacer_gastos_con_medios_pago(df_gastos, df_medios_pago):
    print("\n Union de gastos con medios de pago")
    gastos_con_medio = df_gastos.merge(
        df_medios_pago[['medio_id', 'nombre_medio','tipo']],
        on='medio_id',
        how='left',
    )
    return gastos_con_medio

def hacer_gastos_con_usuarios(df_gastos, df_usuarios):
    print("\n Union de gastos con usuarios")
    gastos_con_usuario = df_gastos.merge(
        df_usuarios[['usuario_id', 'nombre','apellido','email','ciudad','edad']],
        on='usuario_id',
        how='left',
    )

    print(f"Filas en gastos_con_usuario: {len(gastos_con_usuario)}")
    return gastos_con_usuario