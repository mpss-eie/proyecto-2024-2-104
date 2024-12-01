# Análisis y Conclusiones

## 1. Determinación de la Función de Densidad de Probabilidad (FDP)

### Análisis

A partir de los procedimientos realizados y a paritir de los programas creados, primero se logró determinar que el modelo de distribución de mejor ajuste para los datos recopilados es de tipo exponencial. Se obtuvieron los parámetros de loc y scale para cada instante de tiempo en el que se jalaron los datos de la API. 

Como bien se determinó, la media cambiaba respecto al tiempo, específicamente de las condiciones de luz del día y la noche. Al observar el gráfico de promedio contra tiempo, se determinó que esta se mantenía relativamente constante alrededor de 1 cuando es de noche y formaba una curva cuadrática cuando era de día. Al obtener la curva de mejor ajuste de esta cuadrática se pudo obtener una ecuación de la media en función del tiempo, de tal manera que, al realizar el inverso de la media temporal se encontró el parámetro lambda ($\lambda(t)$) necesario para la  PDF de un modelo de distribución exponencial.

Se utilizó la media para obtener la función de densidad de probabilidad en lugar de los parámetros loc y scale debido a que, el parámetro loc típicamente es cero, por lo que este se despreció y, según la documentación el parámetro scale es igual a la media para el tipo de distribución que se está trabajando, es por ello que, por simplicidad se decidió aprovechar la media.

---

## 2. Determinación de la Estacionaridad en Sentido Amplio (WSS) y Ergodicidad

### Análisis
**Estacionaridad:**

- Para \( sunlight = 0 \), el proceso cumple con las condiciones de WSS, ya que la media y la autocorrelación son constantes o dependen únicamente del diferencial de tiempo $\tau$ que, en este caso fue de aproximadamente 42 minutos.
- Para \( sunlight = 1 \), el proceso no es estacionario debido a la variabilidad temporal de la media y la potencia, es decir que el proceso varía con el tiempo, por lo que es muy sencillo indicar que el proceso no es estacionario en su totalidad.

**Ergodicidad:**

- En \( sunlight = 0 \), la media temporal (\( \overline{x} \)) es igual a la media estadística (\( \overline{X} \)), confirmando la ergodicidad en condiciones nocturnas cuando el proceso es confirmado como estacionario en sentido amplio.
- Para \( sunlight = 1 \), la no estacionaridad limita la evaluación ergódica directa pero se puede confirmar que, para las condiciones nocturnas el proceso no es ergódico.

### Implicación
El comportamiento estacionario y ergódico en \( sunlight = 0 \) simplifica el análisis y diseño de sistemas. Sin embargo, las condiciones diurnas requieren métodos más avanzados para predecir y modelar el proceso.

---

## 3. Determinación de Potencia Promedio

### Análisis
**Para \( sunlight = 0 \):**

- La potencia promedio es constante (\( P = 2.00 \)), lo que refleja la estabilidad del proceso en condiciones nocturnas. Dado que el proceso era estacionario en sentido amplio, el cuadrado de los datos durante la noche también es estacionario en sentido amplio, es por ello que la potencia promedio se obtuvo simplemente como el valor esperado del valor cuadrático medio o la media del cuadrado $E[\overline{X^{2}}]$.

**Para \( sunlight = 1 \):**

- La potencia promedio varía cuadráticamente con el tiempo. El ajuste cuadrático permite calcular un valor promedio temporal (\( P = 11.1619 \)), reflejando mayor intensidad durante el día. Dado que el proceso durante el día es dinámico o que varía con el tiempo, fue necesario aplicar la media del valor cuadrático medio a través de integrales y la ecuación de mejor ajuste de los datos.

### Implicación
La potencia promedio estática valida la estabilidad del proceso durante la noche, mientras que el ajuste cuadrático captura de manera efectiva la dinámica diurna.

---

## Conclusiones Generales

1. **Modelo Estadístico**  
   La distribución mejor ajustada a los datos obtenidos de la API fue un factor influyente en la toma de decisiones para el resto de pasos del proyecto. Debido a la simplicidad del modelo exponencial, no fue necesario comprobar el comportamiento temporal de los parámetros brindados por ```fit``` ya que habría sido un doble trabajo. 

2. **Estabilidad y Variabilidad**  
   El proceso es estacionario y ergódico durante la noche (\( sunlight = 0 \)), mientras que en el día (\( sunlight = 1 \)), su complejidad requiere enfoques avanzados para análisis y predicción. En telecomunicaciones y el estudio de procesos complejos y variantes con el tiempo, factores como el clima, las condiciones de luz entre otros pueden dictar el comportamiento de un proceso, es por ello que, para poder intentar predecir lo que sucederá con un determinado proceso, transmisión, u estadística se deben tomar en cuenta todas estas variables tanto dinámicas como estáticas.

3. **Potencia Promedio**  
   La estabilidad nocturna de la potencia promedio simplifica los cálculos y análisis. El ajuste cuadrático para el día ofrece una herramienta útil para modelar variaciones temporales.

4. **Recomendaciones**  
   a) Ampliar el análisis a más variables o condiciones para validar y refinar los modelos actuales.  
   b) Incorporar técnicas avanzadas como análisis espectral o wavelets para abordar la no estacionaridad en \( sunlight = 1 \).
