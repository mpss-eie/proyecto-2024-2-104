import sqlite3

# Conexión a la base de datos
db_path = 'proyecto.db'  # Asegúrate de que el archivo esté en el mismo directorio o proporciona la ruta completa
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Verificar si la columna 'data_squared' ya existe
cursor.execute("PRAGMA table_info(test_data)")
columns = [info[1] for info in cursor.fetchall()]
if 'data_squared' not in columns:
    # Agregar la nueva columna 'data_squared'
    cursor.execute("ALTER TABLE test_data ADD COLUMN data_squared REAL")
    print("Columna 'data_squared' añadida con éxito.")

# Calcular el cuadrado de 'data' y actualizar la columna 'data_squared'
cursor.execute("UPDATE test_data SET data_squared = data * data")
print("Columna 'data_squared' actualizada con el cuadrado de 'data'.")

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
print("Conexión a la base de datos cerrada.")
