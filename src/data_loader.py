import pandas as pd
import sqlalchemy
from config import SQL_MAIN, SQL_BLINDAJE

def conectar_sql(server, database):
    conn_string = (
        f"mssql+pyodbc://@{server}/{database}"
        "?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )
    return sqlalchemy.create_engine(conn_string)

def leer_conversaciones():
    engine = conectar_sql(SQL_MAIN["server"], SQL_MAIN["database"])
    query = """
    SELECT [Ticket], [Texto de interacción], [Asesor],
           [Fecha ticket - Hora ticket], [Grupo]
    FROM [CONVERSACIONES LARAIGO]
    """
    return pd.read_sql(query, engine)

def leer_blindaje():
    engine = conectar_sql(SQL_BLINDAJE["server"], SQL_BLINDAJE["database"])
    query = """
    SELECT TICKET, [Nivel 1], [Nivel 2], [Nivel 3], [Nivel 4], [BaseName]
    FROM [dbo].[TICKETS_PROCESADOS]
    """
    df = pd.read_sql(query, engine)
    df.rename(columns={"TICKET": "ticket"}, inplace=True)
    return df
