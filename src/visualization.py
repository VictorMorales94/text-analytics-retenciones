import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from config import COMPETIDORES

def plot_operadores(df, origen, agrupacion):
    for operador in COMPETIDORES:
        op = operador.upper()
        df_op = df[df["operadores"].apply(lambda ops: op in ops)]

        if df_op.empty:
            continue

        conteo = (
            df_op.groupby("periodo")["ticket"]
                 .nunique()
                 .reset_index()
                 .rename(columns={"ticket": "cantidad"})
        )

        plt.figure(figsize=(12, 6))
        ax = sns.barplot(data=conteo, x="periodo", y="cantidad", palette="Set2")

        for p in ax.patches:
            h = p.get_height()
            if h > 0:
                ax.annotate(f"{int(h)}", (p.get_x() + p.get_width() / 2, h),
                            ha="center", va="bottom", fontsize=8)

        plt.title(f"Ocurrencias - {op}", fontsize=16)
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.savefig(f"graf_{operador}_{origen}_{agrupacion}.png", dpi=300)
        plt.close()

def plot_tortas(df, origen):
    df_ex = df.explode("operadores")
    conteo = df_ex["operadores"].value_counts()

    plt.figure(figsize=(7,7))
    plt.pie(conteo, labels=conteo.index, autopct="%1.1f%%", startangle=140)
    plt.title("Participación total por operadores")
    plt.savefig(f"torta_operadores_{origen}.png")
    plt.close()
