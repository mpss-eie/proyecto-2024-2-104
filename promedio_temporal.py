import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Conectar a la base de datos y cargar la tabla en un DataFrame
conn = sqlite3.connect('proyecto.db')
df = pd.read_sql_query("SELECT * FROM test_data", conn)

# Asegurarse de que la columna 'minutes_from_midnight' esté calculada
# (debe estar calculada previamente como en los pasos anteriores)

# Agrupamos los datos en bloques de 100 elementos
df['group'] = df.index // 100  # Crear un grupo por cada 100 datos

# Calcular el promedio de 'data' para cada grupo de 100 datos y asociarlo con 'minutes_from_midnight'
grouped_data_avg = df.groupby('group').agg(
    avg_data=('data', 'mean'),  # Promedio de la columna 'data'
    minutes_from_midnight=('minutes_from_midnight', 'first'),  # Tomamos el primer valor de 'minutes_from_midnight' para cada grupo
    sunlight=('sunlight', 'first')  # Tomamos el primer valor de 'sunlight' para cada grupo
)

# Crear una lista de colores basada en la columna 'sunlight'
grouped_data_avg['color'] = grouped_data_avg['sunlight'].apply(lambda x: 'orange' if x else 'blue')

# Graficar el promedio de 'data' a lo largo de 'minutes_from_midnight'
plt.figure(figsize=(10, 6))

# Graficamos con los colores basados en 'sunlight'
for i, row in grouped_data_avg.iterrows():
    plt.scatter(row['minutes_from_midnight'], row['avg_data'], color=row['color'])

# Etiquetas y título
plt.xlabel('Minutos desde la Medianoche')
plt.ylabel('Promedio de la Columna "data"')
plt.title('Promedio de los Datos a lo Largo del Tiempo con Influencia del "Sunlight"')

# Agregar leyenda
plt.scatter([], [], color='orange', label='Sunlight')
plt.scatter([], [], color='blue', label='No Sunlight')
plt.legend()

# Mostrar la gráfica
plt.grid(True)
plt.show()

# Cerrar la conexión a la base de datos
conn.close()
