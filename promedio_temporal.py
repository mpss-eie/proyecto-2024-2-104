import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
import os

# Verificar el directorio actual
print(f"Directorio actual: {os.getcwd()}")

# 1. Conectar a la base de datos y cargar la tabla en un DataFrame
try:
    conn = sqlite3.connect('proyecto.db')
    print("Conexión a la base de datos establecida.")
    df = pd.read_sql_query("SELECT * FROM test_data", conn)
    print(f"Datos cargados correctamente. Total de filas: {len(df)}")
except Exception as e:
    print(f"Error al conectar a la base de datos o cargar los datos: {e}")
    exit()

# 2. Agrupar los datos en bloques de 100
try:
    df['group'] = df.index // 100
    grouped_data_avg = df.groupby('group').agg(
        avg_data=('data', 'mean'),
        minutes_from_midnight=('minutes_from_midnight', 'first'),
        sunlight=('sunlight', 'first')
    )
    print("Datos agrupados correctamente.")
except Exception as e:
    print(f"Error al agrupar los datos: {e}")
    exit()

########### Generar la gráfica original ###########

try:
    # Graficar los datos originales
    plt.figure(figsize=(12, 6))

    # Graficar puntos originales con colores según 'sunlight'
    for _, row in grouped_data_avg.iterrows():
        plt.scatter(row['minutes_from_midnight'], row['avg_data'], color='orange' if row['sunlight'] else 'blue')

    # Etiquetas y título
    plt.xlabel('Minutos desde la medianoche')
    plt.ylabel('Promedio de la Columna "data"')
    plt.title('Gráfico original (sin ajuste)')
    plt.grid(True)

    # Agregar leyenda
    plt.scatter([], [], color='orange', label='Sunlight')
    plt.scatter([], [], color='blue', label='No Sunlight')
    plt.legend()

    # Guardar la gráfica original
    plt.savefig('grafico_original.png', dpi=300)
    print("Gráfico original guardado como 'grafico_original.png'.")
    plt.close()
except Exception as e:
    print(f"Error al generar o guardar la gráfica original: {e}")
    exit()

########### Generar la gráfica ajustada con offset y mejor ajuste ###########

try:
    # Parámetro de corrimiento
    offset = 1400

    # Aplicar el corrimiento
    grouped_data_avg['adjusted_minutes'] = grouped_data_avg['minutes_from_midnight'].apply(
        lambda x: x + offset if x < 0 else x
    )

    # Filtrar solo los puntos con 'sunlight = True'
    filtered_data = grouped_data_avg[grouped_data_avg['sunlight'] == True]

    # Variables independientes (x) y dependientes (y) para la curva de mejor ajuste
    x = filtered_data['adjusted_minutes']
    y = filtered_data['avg_data']

    # Ajuste de una curva polinómica (grado 2)
    coefficients = np.polyfit(x, y, deg=2)
    polynomial = np.poly1d(coefficients)
    print("Coeficientes de la curva ajustada:", coefficients)

    # Generar valores para la curva ajustada
    x_curve = np.linspace(x.min(), x.max(), 500)
    y_curve = polynomial(x_curve)

    # Crear la ecuación de la curva en formato texto
    equation = f"y = {coefficients[0]:.6f}x² + {coefficients[1]:.6f}x + {coefficients[2]:.6f}"

    # Graficar los datos ajustados
    plt.figure(figsize=(12, 6))

    # Graficar puntos ajustados (solo Sunlight) - etiqueta solo una vez
    plt.scatter(filtered_data['adjusted_minutes'], filtered_data['avg_data'], color='orange', label='Sunlight')

    # Graficar la curva de mejor ajuste
    plt.plot(x_curve, y_curve, color='green', linewidth=2, label='Curva de mejor ajuste')

    # Agregar la ecuación al gráfico
    plt.text(x.min(), y.max() - 0.3, equation, fontsize=10, color='green', verticalalignment='top')

    # Etiquetas y título
    plt.xlabel('Minutos ajustados desde la medianoche')
    plt.ylabel('Promedio de la Columna "data"')
    plt.title(f'Gráfico ajustado con corrimiento de {offset} minutos hacia la derecha (solo Sunlight)')
    plt.grid(True)

    # Agregar leyenda
    plt.legend()

    # Guardar la gráfica ajustada
    plt.savefig('grafico_ajustado_mejor_ajuste.png', dpi=300)
    print("Gráfico ajustado guardado como 'grafico_ajustado_mejor_ajuste.png'.")
    plt.close()
except Exception as e:
    print(f"Error al generar o guardar la gráfica ajustada: {e}")
    exit()

# Cerrar la conexión a la base de datos
conn.close()
print("Conexión a la base de datos cerrada.")
