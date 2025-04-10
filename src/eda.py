import pandas as pd
import sqlite3
import os
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------- CONFIGURACIÓN ------------------- #

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(SCRIPT_DIR, "..", "online_retail.db")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "..", "docs")

# Asegurar que el directorio exista
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------- CARGA DE DATOS ------------------- #

conn = sqlite3.connect(DB_PATH)
df = pd.read_sql_query("SELECT * FROM transactions", conn)
conn.close()

# Asegurar formatos correctos
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['Total'] = df['Quantity'] * df['UnitPrice']

# ------------------- GRÁFICA 1: Top 10 productos más vendidos ------------------- #

top_products = (
    df.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette="viridis")
plt.title("Top 10 productos más vendidos")
plt.xlabel("Cantidad total vendida")
plt.ylabel("Producto")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "grafica_1_top_productos.png"))
plt.close()

# ------------------- GRÁFICA 2: Dispersión Ingreso vs. Cantidad ------------------- #

# Calcular ingreso por transacción
df["Total"] = df["Quantity"] * df["UnitPrice"]

# Crear gráfico de dispersión para todos los productos
plt.figure(figsize=(10, 6))
plt.scatter(df["Quantity"], df["Total"], alpha=0.5, s=10)
plt.title("Relación entre cantidad vendida e ingreso (todos los productos)")
plt.xlabel("Cantidad vendida por transacción")
plt.ylabel("Ingreso por transacción (£)")
plt.grid(True)
plt.tight_layout()
plt.savefig("docs/grafica_2_global_dispersion_ingreso_cantidad.png")
plt.close()


# ------------------- GRÁFICA 3: Evolución mensual de ventas ------------------- #

df['Month'] = df['InvoiceDate'].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby('Month')['Total']
    .sum()
    .reset_index()
)

plt.figure(figsize=(12, 6))
sns.lineplot(data=monthly_sales, x='Month', y='Total', marker='o')
plt.xticks(rotation=45)
plt.title("Evolución mensual de las ventas")
plt.xlabel("Mes")
plt.ylabel("Total de ventas (£)")
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "grafica_3_ventas_mensuales.png"))
plt.close()