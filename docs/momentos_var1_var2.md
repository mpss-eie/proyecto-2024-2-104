# Momentos de probabilidad de los datos

En esta sección presentamos los momentos estadísticos calculados para `variable_1` y `variable_2` usando dos conjuntos de datos diferentes: un conjunto de datos recolectados durante 12 horas usando los programas `tasks.py` y `models.py` y el otro corresponde a una muestra más pequeña de 50 datos con el fin de aproximar el cálculo de los momentos a mano.

## Momentos de `variable_1` y `variable_2`

Para obtener los momentos de las variables se empleó el siguiente código de python que ameritó el uso de pandas, sqalchemy y scipy.
```python title="calculo_momentos.py"
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

```
### Conjunto de datos de 12 horas

| Momento                 | `variable_1` | `variable_2` |
|-------------------------|--------------|--------------|
| **Media**               | 0.806390     | 1.807410     |
| **Varianza**            | 0.157145     | 1.006807     |
| **Desviación Estándar**  | 0.396416     | 1.003398     |
| **Inclinación (Skewness)** | 1.654464  | 13.782215    |
| **Kurtosis**            | 8.756279     | 768.092391   |

### Muestra de 50 datos

| Momento                 | `variable_1`  | `variable_2`  |
|-------------------------|---------------|---------------|
| **Media**               | 0.845897      | 1.868556      |
| **Varianza**            | 0.156136      | 0.856203      |
| **Desviación Estándar**  | 0.395141      | 0.925312      |
| **Inclinación (Skewness)** | 1.508591   | 2.791238      |
| **Kurtosis**            | 5.875395      | 12.276760     |

## Interpretación Comparativa

- **Media**: Las medias son relativamente similares entre los dos conjuntos de datos. `Variable_2` tiene un valor más alto en ambas muestras.
  
- **Varianza y Desviación Estándar**: `Variable_2` muestra una mayor variabilidad en ambas muestras, pero en la muestra de 50 datos, los valores son algo menores en comparación con el conjunto de 12 horas. Esto indica que la dispersión de los datos es más significativa en el conjunto más grande.

- **Inclinación (Skewness)**: El sesgo de `Variable_2` es extremadamente alto en el conjunto de 12 horas (13.78) y más moderado en la muestra de 50 datos (2.79), lo que podría indicar la presencia de valores atípicos en el conjunto mayor. Esto sugiere una distribución altamente asimétrica en el conjunto de 12 horas.

- **Kurtosis**: La kurtosis de `Variable_2` en el conjunto de 12 horas es muy alta (768.09), lo que sugiere que la distribución tiene picos extremadamente pronunciados y una gran cantidad de valores atípicos. En la muestra de 50 datos, la kurtosis sigue siendo alta (12.28) pero considerablemente menor, lo que indica que la muestra más pequeña no refleja completamente la presencia de valores extremos.


