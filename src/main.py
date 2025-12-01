import pandas as pd
from datetime import datetime

from data_loader import leer_conversaciones, leer_blindaje
from preprocess import limpiar_columnas, convertir_fechas, filtrar_mes, filtrar_origen
from keyword_engine import convertir_a_regex, buscar_palabras, aplicar_operadores
from visualization import plot_operadores, plot_tortas

def run_pipeline(palabras_clave, origen, agrupacion, mes):

    print("📥 Cargando datos...")
    df = leer_conversaciones()
    df = limpiar_columnas(df)
    df = convertir_fechas(df)

    mes_dt = pd.to_datetime(f"{mes}-01")
    df = filtrar_mes(df, mes_dt, agrupacion)

    df["texto_de_interacción"] = df["texto_de_interacción"].str.lower()

    df = filtrar_origen(df, origen)

    palabras_regex = [convertir_a_regex(p) for p in palabras_clave]
    df = buscar_palabras(df, palabras_regex)
    df = aplicar_operadores(df)

    print("📊 Generando gráficos...")
    plot_operadores(df, origen, agrupacion)
    plot_tortas(df, origen)

    print("🎉 Proceso completado.")

if __name__ == "__main__":
    palabras = ["error", "queja"]
    run_pipeline(palabras, "cliente", "diaria", "2025-10")
