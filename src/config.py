import locale

# Configuración regional
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.utf8')
except:
    locale.setlocale(locale.LC_TIME, 'Spanish_Spain')

# Conexiones SQL
SQL_MAIN = {
    "server": "172.17.248.17",
    "database": "BBD_TEXT"
}

SQL_BLINDAJE = {
    "server": "172.17.248.17",
    "database": "WSP_BLINDAJE_PARTNER"
}

# Competidores detectables
COMPETIDORES = ["movistar", "bitel", "entel"]

# Opciones válidas
ORIGENES_VALIDOS = ["cliente", "ejecutivo"]
AGRUPACIONES_VALIDAS = ["diaria", "semanal", "mensual"]
