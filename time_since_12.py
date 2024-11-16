import pandas as pd
import sqlite3

# Conectar a la base de datos y cargar la tabla en un DataFrame
conn = sqlite3.connect('proyecto.db')
df = pd.read_sql_query("SELECT * FROM test_data", conn)

# Convertir 'timestamp' a formato datetime si no lo está ya
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Definir la medianoche del 14 de noviembre de 2024 (sin necesidad de recalcular en cada fila)
midnight_nov_14 = pd.to_datetime('2024-11-14 00:00:00')

# Vectorización: Calcular los minutos en función de si es antes o después de la medianoche
before_midnight = df['timestamp'] < midnight_nov_14
after_midnight = ~before_midnight

# Calcular minutos negativos para los valores antes de la medianoche
df.loc[before_midnight, 'minutes_from_midnight'] = (df.loc[before_midnight, 'timestamp'] - midnight_nov_14).dt.total_seconds() / 60

# Calcular minutos positivos para los valores después de la medianoche
df.loc[after_midnight, 'minutes_from_midnight'] = (df.loc[after_midnight, 'timestamp'] - midnight_nov_14).dt.total_seconds() / 60

# Depuración limitada a las primeras filas
print("Ejemplo de cálculos:")
print(df[['timestamp', 'minutes_from_midnight']].head(10))

# Guardar el DataFrame actualizado en la base de datos
df.to_sql('test_data', conn, if_exists='replace', index=False)
conn.close()

print("Base de datos actualizada con la nueva columna 'minutes_from_midnight'.")
