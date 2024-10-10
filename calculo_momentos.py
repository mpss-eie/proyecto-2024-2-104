import pandas as pd
from sqlalchemy import create_engine
from scipy.stats import skew, kurtosis

# Conectar a la base de datos usando SQLAlchemy
engine = create_engine('sqlite:///proyecto.db')

# Leer los datos de la tabla 'test_data'
df = pd.read_sql("SELECT variable_1, variable_2 FROM test_data", engine)

# Calcular momentos
def calcular_momentos(serie):
    momentos = {
        'promedio': serie.mean(),
        'varianza': serie.var(),
        'desviacion_estandar': serie.std(),
        'inclinacion': skew(serie),
        'kurtosis': kurtosis(serie)
    }
    return momentos

# Aplicar a las dos columnas
momentos_variable_1 = calcular_momentos(df['variable_1'])
momentos_variable_2 = calcular_momentos(df['variable_2'])

# Mostrar los resultados
# Función para imprimir los resultados de manera ordenada
def mostrar_momentos(nombre_variable, momentos):
    print(f"\nMomentos de {nombre_variable}:")
    print(f"Promedio:             {momentos['promedio']:.6f}")
    print(f"Varianza:             {momentos['varianza']:.6f}")
    print(f"Desviación Estándar:  {momentos['desviacion_estandar']:.6f}")
    print(f"Inclinación (Skew):   {momentos['inclinacion']:.6f}")
    print(f"Kurtosis:             {momentos['kurtosis']:.6f}")


# Mostrar los resultados de manera ordenada
mostrar_momentos('variable_1', momentos_variable_1)
mostrar_momentos('variable_2', momentos_variable_2)
