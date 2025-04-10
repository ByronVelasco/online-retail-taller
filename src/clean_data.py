import pandas as pd
import os

# ------------------- CONFIGURACIÓN DE RUTAS ------------------- #

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(SCRIPT_DIR, "..", "data", "Online_Retail.xlsx")
OUTPUT_PATH = os.path.join(SCRIPT_DIR, "..", "cleaned_data", "online_retail_clean.csv")

# ------------------- CARGA DE DATOS ------------------- #

print("Leyendo archivo Excel...")
df = pd.read_excel(DATA_PATH, engine="openpyxl")
print(f"Total de registros cargados: {len(df)}")

# ------------------- LIMPIEZA DE DATOS ------------------- #

# 1. Eliminar duplicados
df = df.drop_duplicates()

# 2. Eliminar filas con nulos en columnas claves
#StockCode y CustomerID tienen NA
#Las otras columnas no tienen NA, y si los tienen, se pueden asignar un valor con respecto a otra columna
columns_to_check = ['StockCode', 'CustomerID']
df = df.dropna(subset=columns_to_check)

# 3. Eliminar cancelaciones (InvoiceNo que comienza con "C")
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')]

# 4. Filtrar Quantity y UnitPrice > 0
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# 5. Forzar formatos de datos
df['InvoiceNo'] = df['InvoiceNo'].astype(int) #Categoría
df['StockCode'] = df['StockCode'].astype(str) #Categoría
df['Description'] = df['Description'].astype(str) #Categoría
df['Quantity'] = df['Quantity'].astype(int) #Entero
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate']) #Fecha
df['UnitPrice'] = df['UnitPrice'].astype(float) #Decimal
df['CustomerID'] = df['CustomerID'].astype(int) #Categoría
df['Country'] = df['Country'].astype(str) #Categoría

# 6. Normalizar texto en columnas categóricas
df['Description'] = df['Description'].str.strip().str.upper() #Eliminar espacios y convertir a mayúsculas
df['Country'] = df['Country'].str.strip().str.upper() #Eliminar espacios y convertir a mayúsculas

# 7. Corregir descripciones inválidas que contienen "?" usando StockCode
print("Corrigiendo descripciones inválidas con '?'...")

# Crear diccionario StockCode -> Description (solo de registros válidos)
valid_descriptions = (
    df[~df['Description'].str.contains('\?', na=True)]
    .drop_duplicates(subset=['StockCode'])
    .set_index('StockCode')['Description']
    .to_dict()
)

# Función para reemplazar descripciones inválidas
def corregir_descripcion(row):
    if pd.isna(row['Description']) or '?' in row['Description']:
        return valid_descriptions.get(row['StockCode'], row['Description'])
    return row['Description']

# Aplicar corrección
df['Description'] = df.apply(corregir_descripcion, axis=1)

# 8. Reemplazar "UNSPECIFIED" por "UNITED KINGDOM" en la columna Country
df['Country'] = df['Country'].replace("UNSPECIFIED", "UNITED KINGDOM")

# ------------------- RESULTADO FINAL ------------------- #

print(f"Total de registros luego de limpieza: {len(df)}")
df.to_csv(OUTPUT_PATH, index=False)
print("Archivo limpio guardado en:", OUTPUT_PATH)