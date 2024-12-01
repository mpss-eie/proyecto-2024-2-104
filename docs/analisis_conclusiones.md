# Análisis y Conclusiones

## 1. Determinación de la Función de Densidad de Probabilidad (FDP)

### Análisis
Los histogramas de las variables muestran los siguientes comportamientos:

- **Variable 1**: Sigue una **distribución Rayleigh**, lo que sugiere que está influenciada por la suma cuadrática de variables aleatorias independientes.
- **Variable 2**: Se ajusta a una **distribución exponencial**, característica de procesos con tasas constantes de ocurrencia de eventos.

En el caso de \( sunlight = 1 \), los datos también se ajustan a un modelo exponencial, validado mediante histogramas y ajustes de densidad.

### Implicación
Las distribuciones identificadas permiten modelar fenómenos reales y realizar simulaciones para procesos aleatorios que compartan características similares.

---

## 2. Determinación de la Estacionaridad en Sentido Amplio (WSS) y Ergodicidad

### Análisis
**Estacionaridad:**

- Para \( sunlight = 0 \), el proceso cumple con las condiciones de WSS, ya que la media y la autocorrelación son constantes o dependen únicamente del diferencial de tiempo.
- Para \( sunlight = 1 \), el proceso no es estacionario debido a la variabilidad temporal de la media y la potencia.

**Ergodicidad:**

- En \( sunlight = 0 \), la media temporal (\( \overline{x} \)) es igual a la media estadística (\( \overline{X} \)), confirmando la ergodicidad en condiciones nocturnas.
- Para \( sunlight = 1 \), la no estacionaridad limita la evaluación ergódica directa.

### Implicación
El comportamiento estacionario y ergódico en \( sunlight = 0 \) simplifica el análisis y diseño de sistemas. Sin embargo, las condiciones diurnas requieren métodos más avanzados para predecir y modelar el proceso.

---

## 3. Determinación de Potencia Promedio

### Análisis
**Para \( sunlight = 0 \):**

- La potencia promedio es constante (\( P = 2.00 \)), lo que refleja la estabilidad del proceso en condiciones nocturnas.

**Para \( sunlight = 1 \):**

- La potencia promedio varía cuadráticamente con el tiempo. El ajuste cuadrático permite calcular un valor promedio temporal (\( P = 11.1619 \)), reflejando mayor intensidad durante el día.

### Implicación
La potencia promedio estática valida la estabilidad del proceso durante la noche, mientras que el ajuste cuadrático captura de manera efectiva la dinámica diurna.

---

## Conclusiones Generales

1. **Modelo Estadístico**  
   Las distribuciones identificadas (Rayleigh y exponencial) describen con precisión el comportamiento de las variables, facilitando la simulación de fenómenos reales.

2. **Estabilidad y Variabilidad**  
   El proceso es estacionario y ergódico durante la noche (\( sunlight = 0 \)), mientras que en el día (\( sunlight = 1 \)), su complejidad requiere enfoques avanzados para análisis y predicción.

3. **Potencia Promedio**  
   La estabilidad nocturna de la potencia promedio simplifica los cálculos y análisis. El ajuste cuadrático para el día ofrece una herramienta útil para modelar variaciones temporales.

4. **Recomendaciones**  
   a) Ampliar el análisis a más variables o condiciones para validar y refinar los modelos actuales.  
   b) Incorporar técnicas avanzadas como análisis espectral o wavelets para abordar la no estacionaridad en \( sunlight = 1 \).
