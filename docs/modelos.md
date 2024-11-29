# Modelos de probabilidad de los datos

En esta sección presentamos los momentos estadísticos calculados para `variable_1` y `variable_2` usando dos conjuntos de datos diferentes: un conjunto de datos recolectados durante 12 horas y una muestra más pequeña de 50 datos.

## Momentos de `variable_1` y `variable_2`

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

## Borramos esto Dario?
Una parte central del proyecto es modelar estadísticamente los datos con distribuciones de probabilidad.

En el `PyX` número 5 [Py5](https://github.com/fabianabarca/python) hay una discusión sobre modelado de datos con SciPy y Fitter.

En general, con el módulo `stats` del paquete SciPy es posible encontrar los parámetros de mejor ajuste para una distribución particular, utilizando el método `fit()` de las clases de variables aleatorias. Por ejemplo, para una distribución normal:

```python
from scipy import stats

params = stats.norm.fit(data)

print(params)
```

donde `data` es un conjunto de datos univariados.

