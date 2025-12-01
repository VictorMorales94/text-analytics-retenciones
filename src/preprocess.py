import pandas as pd
from config import ORIGENES_VALIDOS

def limpiar_columnas(df):
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
                  .str.replace("-", "_")
    )
    return df

def filtrar_origen(df, origen):
    if origen == "cliente":
        return df[df["asesor"].str.lower().isin(["cliente"])]
    else:
        return df[~df["asesor"].str.lower().isin(["cliente", "bot system"])]

def convertir_fechas(df):
    df["fecha_ticket"] = pd.to_datetime(df["fecha_ticket___hora_ticket"])
    return df

def filtrar_mes(df, mes_dt, agrupacion):
    if agrupacion in ["diaria", "semanal"]:
        df = df[df["fecha_ticket"].dt.to_period('M') == mes_dt.to_period("M")]
    return df
