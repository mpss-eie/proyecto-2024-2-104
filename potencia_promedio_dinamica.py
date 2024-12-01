import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Conectar a la base de datos
db_path = 'proyecto.db'  # Asegúrate de poner la ruta correcta de tu archivo .db
conn = sqlite3.connect(db_path)

# Consultar los datos necesarios, excluyendo sunlight = 0
query = '''
SELECT minutes_from_midnight, AVG(data_squared) as avg_data_squared
FROM test_data
WHERE sunlight = 1
GROUP BY minutes_from_midnight
'''

# Leer los resultados en un DataFrame
df = pd.read_sql(query, conn)

# Cerrar la conexión a la base de datos
conn.close()

# Ajustar los valores negativos de minutes_from_midnight
df['adjusted_minutes_from_midnight'] = df['minutes_from_midnight'].apply(lambda x: x + 1400 if x < 0 else x)

# Variables para el ajuste
x = df['adjusted_minutes_from_midnight']
y = df['avg_data_squared']

# Ajuste polinomial de grado 2
coefficients = np.polyfit(x, y, deg=2)  # Encuentra los coeficientes a, b, c de la ecuación ax^2 + bx + c
polynomial = np.poly1d(coefficients)   # Genera el polinomio

# Definir la función para integrar
def f(x):
    return coefficients[0] * x**2 + coefficients[1] * x + coefficients[2]

# Calcular el promedio temporal
a, b = x.min(), x.max()  # Límite inferior y superior del intervalo
integral_value, _ = quad(f, a, b)  # Calcular la integral
temporal_average = integral_value / (b - a)  # Promedio temporal

# Crear la ecuación en formato legible
equation = f"$y = {coefficients[0]:.4f}x^2 + {coefficients[1]:.4f}x + {coefficients[2]:.4f}$"

# Crear la gráfica
plt.figure(figsize=(10, 6))

# Graficar los datos ajustados
plt.scatter(x, y, color='orange', label='Datos ajustados (sunlight = 1)', marker='o')

# Graficar la curva de mejor ajuste con la ecuación en la leyenda
x_fit = np.linspace(a, b, 500)  # Valores para evaluar la curva
y_fit = polynomial(x_fit)  # Valores correspondientes de la curva ajustada
plt.plot(x_fit, y_fit, color='blue', label=f'Curva cuadrática ajustada: {equation}')

# Títulos y etiquetas
plt.title('Curva cuadrática de mejor ajuste (sunlight = 1)')
plt.xlabel('Minutes from Midnight (ajustados)')
plt.ylabel('Promedio de data_squared')

# Leyenda y grid
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

# Imprimir resultados
print("Coeficientes de la curva ajustada (ax^2 + bx + c):")
print(f"a = {coefficients[0]:.4f}, b = {coefficients[1]:.4f}, c = {coefficients[2]:.4f}")
print(f"Promedio temporal calculado a partir de la curva de mejor ajuste: {temporal_average:.4f}")
