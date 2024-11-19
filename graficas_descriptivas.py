import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pareto, johnsonsb

# Conectar a la base de datos y cargar la tabla en un DataFrame
conn = sqlite3.connect('proyecto.db')
df = pd.read_sql_query("SELECT * FROM test_data", conn)
conn.close()

# Filtrar todos los datos para minutes_from_midnight = 626.05
target_minutes = 626.05
filtered_data = df[df['minutes_from_midnight'] == target_minutes]['data'].dropna()

# Verificar si hay datos disponibles después del filtro
if filtered_data.empty:
    print(f"No se encontraron datos para minutes_from_midnight = {target_minutes}.")
else:
    # Ajuste a la distribución Pareto
    params_pareto = pareto.fit(filtered_data)
    b, loc, scale = params_pareto
    print(f"Parámetros de la distribución Pareto: b={b:.4f}, loc={loc:.4f}, scale={scale:.4f}")
    
    # Ajuste a la distribución JohnsonSB
    params_johnsonsb = johnsonsb.fit(filtered_data)
    gamma, xi, loc_johnsonsb, scale_johnsonsb = params_johnsonsb
    print(f"Parámetros de la distribución JohnsonSB: gamma={gamma:.4f}, xi={xi:.4f}, loc={loc_johnsonsb:.4f}, scale={scale_johnsonsb:.4f}")
    
    # Crear un histograma de los datos con más bins para mejor visualización
    plt.figure(figsize=(8, 6))
    plt.hist(filtered_data, bins='auto', color='skyblue', edgecolor='black', alpha=0.7, density=True, label='Histograma')

    # Generar los valores de la función de densidad de la distribución Pareto ajustada
    x = np.linspace(min(filtered_data), max(filtered_data), 1000)
    pdf_pareto = pareto.pdf(x, b, loc, scale)

    # Generar los valores de la función de densidad de la distribución JohnsonSB ajustada
    pdf_johnsonsb = johnsonsb.pdf(x, gamma, xi, loc_johnsonsb, scale_johnsonsb)

    # Graficar ambas distribuciones ajustadas
    plt.plot(x, pdf_pareto, 'r-', lw=2, label='Distribución Pareto ajustada')
    plt.plot(x, pdf_johnsonsb, 'g-', lw=2, label='Distribución JohnsonSB ajustada')
    
    # Ajustar el rango de los ejes para mejor visualización
    plt.xlim(min(filtered_data) - 1, max(filtered_data) + 1)  # Rango eje X
    plt.ylim(0, max(pdf_pareto.max(), pdf_johnsonsb.max()) * 1.1)  # Rango eje Y
    
    # Títulos y etiquetas
    plt.title(f"Histograma y ajustes Pareto y JohnsonSB para minutes_from_midnight = {target_minutes}", fontsize=14)
    plt.xlabel("Valores", fontsize=12)
    plt.ylabel("Densidad", fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Mostrar la gráfica
    plt.show()
