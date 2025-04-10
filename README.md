# Online Retail Data Analysis

Este proyecto forma parte del curso **Fundamentos de Ciencia de Datos** y tiene como objetivo realizar una limpieza, análisis exploratorio y visualización de datos sobre transacciones de una tienda de retail en línea.

---

## Estructura del Proyecto

```
online-retail-taller/
│
├── cleaned_data/               # CSV limpio resultante de la limpieza
│   └── online_retail_clean.csv
│
├── data/                       # Datos originales
│   └── Online_Retail.xlsx
│
├── docs/                       # Archivos de documentación y visualizaciones
│   ├── dataset_description.txt
│   ├── visualization_description.txt
│   ├── grafica_1_top_productos.png
│   ├── grafica_2_global_dispersion_ingreso_cantidad.png
│   └── grafica_3_ventas_mensuales.png
│
├── src/                        # Scripts Python del proyecto
│   ├── clean_data.py           # Limpieza y transformación inicial
│   ├── load_to_sqlite.py       # Carga de datos a SQLite
│   └── eda.py                  # Análisis exploratorio y visualización
│
├── online_retail.db            # Base de datos SQLite generada
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Descripción del proyecto
```

---

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

```bash
pip install -r requirements.txt
```

---

## Ejecución

1. **Limpieza de datos**  
   Ejecuta el script para limpiar los datos y generar el CSV limpio:

   ```bash
   python src/clean_data.py
   ```

2. **Carga en base de datos SQLite**  
   Este script carga el CSV limpio en una base de datos SQLite:

   ```bash
   python src/load_to_sqlite.py
   ```

3. **Análisis exploratorio y visualización**  
   Ejecuta el análisis EDA y genera gráficos:

   ```bash
   python src/eda.py
   ```

---

## Resultados

El proyecto genera tres visualizaciones:

- **Gráfica 1**: Top 10 productos más vendidos.
- **Gráfica 2**: Dispersión entre cantidad vendida e ingreso por transacción (todos los productos).
- **Gráfica 3**: Evolución mensual de las ventas.

Estas se encuentran en la carpeta `docs/` y se explican en `visualizaciones_descripcion.txt`.

---

## Autor

Byron Velasco – 2025  
Maestría en Ciencia de Datos