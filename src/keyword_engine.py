import re
import pandas as pd
from config import COMPETIDORES

def convertir_a_regex(palabra):
    if "%" in palabra:
        raiz = re.escape(palabra.replace("%", ""))
        return re.compile(rf"\b{raiz}\w*", re.IGNORECASE)
    return re.compile(rf"\b{re.escape(palabra)}\b", re.IGNORECASE)

def buscar_palabras(df, palabras_regex):
    df["tiene_palabra_clave"] = df["texto_de_interacción"].apply(
        lambda x: any(rgx.search(x) for rgx in palabras_regex)
    )
    return df[df["tiene_palabra_clave"]]

def detectar_operadores(texto):
    return [op.upper() for op in COMPETIDORES if op in texto] or ["SIN OPERADOR"]

def aplicar_operadores(df):
    df["operadores"] = df["texto_de_interacción"].apply(detectar_operadores)
    return df
