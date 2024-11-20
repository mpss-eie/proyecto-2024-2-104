import sqlite3
import pandas as pd
from scipy.stats import expon

# Conexión a la base de datos original
def calculate_and_update_parameters():
    db_path_original = "proyecto.db"  # Base de datos original
    db_path_new = "parametros.db"     # Base de datos con los parámetros

    # Conexión a la base de datos de parámetros
    conn_new = sqlite3.connect(db_path_new)

    # Paso 1: Asegurar que las columnas 'loc' y 'scale' existan en la tabla 'parameter_data'
    try:
        conn_new.execute("PRAGMA foreign_keys=off;")
        conn_new.execute("ALTER TABLE parameter_data ADD COLUMN loc REAL;")
        conn_new.execute("ALTER TABLE parameter_data ADD COLUMN scale REAL;")
        conn_new.execute("PRAGMA foreign_keys=on;")
        conn_new.commit()
        print("Se han añadido las columnas 'loc' y 'scale' a la tabla 'parameter_data'.")
    except sqlite3.Error as e:
        print(f"Error al añadir las columnas: {e}")

    # Conexión a la base original para obtener los datos
    conn_original = sqlite3.connect(db_path_original)

    # Consulta para obtener todos los datos ordenados por timestamp
    query = "SELECT timestamp, minutes_from_midnight, data FROM test_data ORDER BY timestamp"
    data = pd.read_sql_query(query, conn_original)

    # Cerrar conexión a la base original
    conn_original.close()

    # Dividir los datos en bloques de 100 filas
    blocks = [data[i:i + 100] for i in range(0, len(data), 100)]

    # Calcular loc y scale para cada bloque y actualizar la base de datos
    for idx, block in enumerate(blocks):
        # Verificar que el bloque tenga al menos 2 datos
        if len(block) < 2:
            continue

        # Ajustar la distribución exponencial a los datos de 'data' (NO 'minutes_from_midnight')
        try:
            loc, scale = expon.fit(block['data'])
            print(f"Bloque {idx+1}: loc = {loc}, scale = {scale}")
        except Exception as e:
            print(f"Error al ajustar el bloque {idx+1}: {e}")
            continue

        # Obtener el ID correspondiente en parameter_data
        timestamp_first = block['timestamp'].iloc[0]
        query_id = "SELECT id FROM parameter_data WHERE timestamp = ?"
        result = conn_new.execute(query_id, (timestamp_first,)).fetchone()

        # Si el ID no existe, continuar con el siguiente bloque
        if result is None:
            print(f"El timestamp {timestamp_first} no se encontró en la tabla parameter_data.")
            continue

        row_id = result[0]

        # Actualizar los valores loc y scale en la base de datos
        update_query = """
        UPDATE parameter_data
        SET loc = ?, scale = ?
        WHERE id = ?;
        """
        conn_new.execute(update_query, (loc, scale, row_id))

    # Confirmar los cambios y cerrar la conexión
    conn_new.commit()
    conn_new.close()

    print("Se actualizaron los parámetros loc y scale en la base de datos 'parametros.db'.")

if __name__ == "__main__":
    calculate_and_update_parameters()
