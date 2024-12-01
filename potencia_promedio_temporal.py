import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Conectar a la base de datos
db_path = 'proyecto.db'  # Asegúrate de poner la ruta correcta de tu archivo .db
conn = sqlite3.connect(db_path)

# Consultar los datos necesarios, añadiendo 'sunlight'
query = '''
SELECT minutes_from_midnight, AVG(data_squared) as avg_data_squared, sunlight
FROM test_data
GROUP BY minutes_from_midnight, sunlight
'''

# Leer los resultados en un DataFrame
df = pd.read_sql(query, conn)

# Consultar el valor esperado de data_squared para sunlight = 0
expected_query = '''
SELECT AVG(data_squared) as expected_value
FROM test_data
WHERE sunlight = 0
'''
expected_value = pd.read_sql(expected_query, conn).iloc[0, 0]

# Cerrar la conexión a la base de datos
conn.close()

# Gráfica original con todos los datos
plt.figure(figsize=(10, 6))

# Graficar los datos para sunlight == 0
df_sunlight_0 = df[df['sunlight'] == 0]
plt.scatter(df_sunlight_0['minutes_from_midnight'], df_sunlight_0['avg_data_squared'], color='b', label='Sunlight = 0', marker='o')

# Graficar los datos para sunlight == 1 en naranja con círculos
df_sunlight_1 = df[df['sunlight'] == 1]
plt.scatter(df_sunlight_1['minutes_from_midnight'], df_sunlight_1['avg_data_squared'], color='orange', label='Sunlight = 1', marker='o')

# Calcular límites del eje Y
y_min, y_max = df['avg_data_squared'].min(), df['avg_data_squared'].max()

# Ajustar límites del eje Y
plt.ylim(y_min, y_max)

# Títulos y etiquetas
plt.title('Promedio de data_squared en función del tiempo (minutes_from_midnight)')
plt.xlabel('Minutes from Midnight')
plt.ylabel('Promedio de data_squared')

# Leyenda y grid
plt.legend()
plt.grid(True)

# Mostrar la gráfica original
plt.show()

# Gráfica solo para sunlight == 0, manteniendo los límites de los ejes
plt.figure(figsize=(10, 6))

# Graficar los datos para sunlight == 0
plt.scatter(df_sunlight_0['minutes_from_midnight'], df_sunlight_0['avg_data_squared'], color='b', label='Sunlight = 0', marker='o')

# Mostrar el valor esperado como una línea horizontal
plt.axhline(y=expected_value, color='blue', linestyle='--', label=f'Valor esperado (sunlight=0): {expected_value:.2f}')

# Mantener límites del eje Y iguales a la gráfica original
plt.ylim(y_min, y_max)

# Títulos y etiquetas
plt.title('Promedio de data_squared para sunlight = 0 (mismos ejes)')
plt.xlabel('Minutes from Midnight')
plt.ylabel('Promedio de data_squared')

# Leyenda y grid
plt.legend()
plt.grid(True)

# Mostrar la gráfica solo para sunlight == 0
plt.show()

# Imprimir el valor esperado en consola
print(f"El valor esperado (promedio global) de data_squared para sunlight=0 es: {expected_value:.2f}")
