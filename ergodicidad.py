import sqlite3

# Conectar a la base de datos
db_path = "proyecto.db"  # Ruta de tu base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Consulta SQL para obtener el promedio
query = """
WITH RankedData AS (
    SELECT 
        timestamp, 
        data,
        ROW_NUMBER() OVER (PARTITION BY timestamp ORDER BY ROWID) AS row_num
    FROM test_data
    WHERE sunlight = 0
)
SELECT AVG(data) AS average_data
FROM RankedData
WHERE row_num = 1;
"""

# Ejecutar la consulta
cursor.execute(query)
result = cursor.fetchone()

# Mostrar el resultado
average_data = result[0]
print(f"El promedio temporal de la función muestra de los primeros valores de 'data' para cada 'timestamp' con 'sunlight' = 0 es: {average_data}")

# Cerrar la conexión
conn.close()
