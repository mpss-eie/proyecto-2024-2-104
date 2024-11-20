import sqlite3
import pandas as pd

# Conexión a la base de datos existente
db_path = "proyecto.db"  # Cambia este nombre si tu base original tiene otro nombre
conn_original = sqlite3.connect(db_path)

# Consulta para obtener todos los datos ordenados por timestamp
query = "SELECT timestamp, minutes_from_midnight, sunlight FROM test_data ORDER BY timestamp"
data = pd.read_sql_query(query, conn_original)

# Cerrar conexión a la base original
conn_original.close()

# Extraer el timestamp, minutes_from_midnight y sunlight del primer valor de cada bloque de 100 datos
timestamps = data['timestamp'][::100]  # Saltar de 100 en 100
minutes = data['minutes_from_midnight'][::100]
sunlight = data['sunlight'][::100]

# Crear la nueva base de datos
new_db_path = "parametros.db"
conn_new = sqlite3.connect(new_db_path)

# Crear la tabla en la nueva base de datos
create_table_query = """
CREATE TABLE IF NOT EXISTS parameter_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    minutes_from_midnight REAL NOT NULL,
    sunlight REAL NOT NULL
);
"""
conn_new.execute(create_table_query)

# Insertar los timestamps, minutes_from_midnight y sunlight en la nueva tabla
insert_query = """
INSERT INTO parameter_data (timestamp, minutes_from_midnight, sunlight) 
VALUES (?, ?, ?)
"""
for ts, minutes, sl in zip(timestamps, minutes, sunlight):
    conn_new.execute(insert_query, (ts, minutes, sl))

# Confirmar los cambios y cerrar la conexión
conn_new.commit()
conn_new.close()

print("Se creó la base de datos 'parametros.db' sin las columnas 'loc' y 'scale'.")
