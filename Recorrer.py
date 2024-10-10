import sqlite3
import pandas as pd

def fetch_limited_data_from_db(db_path, limit=50):
    # Conectar a la base de datos SQLite
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Obtener todas las tablas en la base de datos
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        print(f"Recuperando datos de la tabla: {table_name}")

        # Obtener los datos de la tabla actual con límite
        cursor.execute(f"SELECT * FROM {table_name} LIMIT {limit}")
        rows = cursor.fetchall()

        # Obtener los nombres de las columnas
        cursor.execute(f"PRAGMA table_info({table_name})")
        column_info = cursor.fetchall()
        column_names = [column[1] for column in column_info]

        # Crear un DataFrame de pandas con los datos
        df = pd.DataFrame(rows, columns=column_names)

        # Exportar los datos a un archivo Excel
        file_name = f"{table_name}_exportado.xlsx"
        df.to_excel(file_name, index=False)
        print(f"Datos de la tabla {table_name} exportados a {file_name}")

    # Cerrar la conexión
    conn.close()

# Ejecutar la función
db_path = 'proyecto.db'  # Cambia esto si el archivo tiene otro nombre o ubicación
fetch_limited_data_from_db(db_path, limit=50)
