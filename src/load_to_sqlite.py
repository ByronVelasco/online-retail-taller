import pandas as pd
import sqlite3
import os

# ------------------- CONFIGURACIÓN DE RUTAS ------------------- #

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta al CSV limpio
CSV_PATH = os.path.join(SCRIPT_DIR, "..", "cleaned_data", "online_retail_clean.csv")

# Ruta a la base de datos SQLite
DB_PATH = os.path.join(SCRIPT_DIR, "..", "online_retail.db")

# ------------------- CARGA Y AJUSTE DEL DATAFRAME ------------------- #

print("Cargando archivo limpio...")
df = pd.read_csv(CSV_PATH, parse_dates=['InvoiceDate'])  # Asegura que la fecha se cargue bien

# Si es necesario, puedes forzar tipos aquí de nuevo
# df['CustomerID'] = df['CustomerID'].astype(int)  # ya debe venir bien

print(f"Registros cargados: {len(df)}")

# ------------------- GUARDADO EN SQLITE ------------------- #

# Conexión a SQLite
conn = sqlite3.connect(DB_PATH)

# Subir a tabla "transactions"
df.to_sql("transactions", conn, if_exists="replace", index=False)

print("Datos guardados en la base de datos SQLite:")
print("Tabla: transactions")
print("Archivo:", DB_PATH)

conn.close()