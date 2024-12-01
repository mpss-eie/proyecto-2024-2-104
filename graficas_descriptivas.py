import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Conectar a la base de datos
db_path = 'proyecto.db'  # Asegúrate de poner la ruta correcta de tu archivo .db
conn = sqlite3.connect(db_path)

# Consultar todos los valores de la columna 'data' con sunlight = 1
query = '''
SELECT data
FROM test_data
WHERE sunlight = 1
'''

# Leer los resultados en un DataFrame
df = pd.read_sql(query, conn)

# Cerrar la conexión a la base de datos
conn.close()

# Extraer los valores de la columna 'data' con sunlight = 1
data_values = df['data'].values

# Graficar el histograma de todos los valores de 'data' con sunlight = 1
plt.figure(figsize=(10, 6))
plt.hist(data_values, bins=20, density=True, alpha=0.6, color='g', label='Histograma')

# Ajustar una distribución exponencial
params = expon.fit(data_values)  # Ajustar una distribución exponencial (parámetros: loc, scale)

# Crear una línea con los valores ajustados
x = np.linspace(min(data_values), max(data_values), 1000)
pdf_fitted = expon.pdf(x, *params)  # Obtener la función de densidad de probabilidad ajustada

# Graficar la distribución exponencial ajustada
plt.plot(x, pdf_fitted, 'r-', label='Ajuste exponencial')

# Títulos y etiquetas
plt.title('Histograma de los datos (sunlight = 1) y ajuste exponencial')
plt.xlabel('Valor de data')
plt.ylabel('Densidad')

# Leyenda y grid
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

# Imprimir los parámetros del ajuste exponencial
print(f"Parámetros del ajuste exponencial: loc = {params[0]:.4f}, scale = {params[1]:.4f}")
