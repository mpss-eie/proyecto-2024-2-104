import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
    # Conexión a la base de datos
    db_path = "proyecto.db"  # Ajusta la ruta si es necesario
    conn = sqlite3.connect(db_path)

    # Consulta SQL para filtrar los datos con sunlight = 0
    query = """
    SELECT minutes_from_midnight 
    FROM test_data 
    WHERE sunlight = 0
    ORDER BY minutes_from_midnight
    """

    # Obtener los datos
    data = pd.read_sql_query(query, conn)

    # Cerrar la conexión
    conn.close()

    # Verificar cuántos datos caen dentro del rango especificado
    block = data[
        (data['minutes_from_midnight'] >= 252.45) & 
        (data['minutes_from_midnight'] <= 294.15)
    ]

    # Verificar si hay suficientes datos en el bloque
    if len(block) < 2:
        print("No hay suficientes datos en el bloque especificado.")
    else:
        print(f"Tamaño del bloque: {len(block)}")
        
        # Extraer la serie de datos
        series = block['minutes_from_midnight'].values
        
        # Calcular la autocorrelación simple entre los datos (sin desfases)
        corr_matrix = np.corrcoef(series[:-1], series[1:])
        autocorr_value = corr_matrix[0, 1]
        
        # Mostrar el valor de autocorrelación
        print(f"Autocorrelación en el intervalo de tiempo de -322.95 a -282.75: {autocorr_value}")

except sqlite3.Error as e:
    print(f"Error al acceder a la base de datos: {e}")
except Exception as e:
    print(f"Ocurrió un error: {e}")