import pandas as pd
import sqlite3
from fitter import Fitter

# Conectar a la base de datos y cargar la tabla en un DataFrame
conn = sqlite3.connect('proyecto.db')
df = pd.read_sql_query("SELECT * FROM test_data", conn)
conn.close()

# Filtrar los datos para minutes_from_midnight = 626.05
target_minutes = 553.5
filtered_data = df[df['minutes_from_midnight'] == target_minutes]['data'].dropna()

# Verificar si hay datos disponibles después del filtro
if filtered_data.empty:
    print(f"No se encontraron datos para minutes_from_midnight = {target_minutes}.")
else:
    # Seleccionar las distribuciones que quieres probar
    distributions = [
        'norm', 'expon', 'gompertz', 'levy',
        'logistic', 'rayleigh'
    ]
    
    # Ajustar las distribuciones a los datos de 'filtered_data'
    f = Fitter(filtered_data, distributions=distributions)
    f.fit()  # Ajusta las distribuciones a los datos

    # Obtener la mejor distribución para estos datos
    best_dist = f.get_best()
    best_dist_name = list(best_dist.keys())[0]  # Nombre de la mejor distribución
    best_dist_params = best_dist[best_dist_name]  # Parámetros de la mejor distribución

    # Imprimir el resultado
    print(f"Para minutes_from_midnight = {target_minutes}, la mejor distribución es: "
          f"{best_dist_name}, con los parámetros: {best_dist_params}")

