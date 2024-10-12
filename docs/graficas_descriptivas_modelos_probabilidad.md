# Recopilación, almacenamiento de datos y gráficas descriptivas

En este apartado se documentará cómo se recopilaron los datos y se explorarán los programas `.py`diseñados para la creación de gráficas e histogramas. A continuación se explicarán las librerías utilizadas para confeccionar la lógica de programación para los programas creados externos a los brindados en el repositorio

### **1. Pandas**

Pandas es una librería de python que facilita la manipulación y el análisis de datos. Proporciona herramientas que facilita el trabajo con tablas de datos.

Enfocado a aspectos del proyecto, pandas permite seleccionar y filtrar, a través de comandos y de forma sencilla los conjuntos de datos que me interesan de una tabla. Por ejemplo los datos de la primera columna o de la segunda según sea el caso.

### **2. SQLalchemy**

SQLAlchemy es una biblioteca de Python para trabajar con bases de datos relacionales. Es un ORM (Object Relational Mapper) que proporciona una capa de abstracción entre el código Python y las bases de datos. Algunas características clave de SQLAlchemy son:

1. Compatibilidad con múltiples bases de datos (MySQL, PostgreSQL, SQLite, etc.)
2. Mapeo objeto-relacional (ORM) para interactuar con la base de datos usando objetos Python
3. Expresión SQL para construir consultas complejas de manera programática
4. Soporte para transacciones y conexiones pooling
5. Herramientas para migración de esquemas de base de datos

### **3. Matplotlib**

Matplotlib es una biblioteca de visualización de datos en Python, diseñada para crear gráficos estáticos, animados e interactivos de alta calidad. Es una de las herramientas más populares para la visualización de datos en el ecosistema científico de Python. Uno de los aspectos más útiles es que permite crear una amplia gama de gráficos, incluyendo gráficos de líneas, de barras, de dispersión, histogramas, gráficos de pastel, gráficos 3D, y muchos más.

En resumen, integra aspectos propios de matlab en el ambiente de python para facilitar la creación de gráficos y el manejo de datos cómo se realiza en la plataforma de matlab.
### Gráficas descriptivas de las variables 1 y 2

A continuación se muestra el código empleado para la generación de los histogramas a partir de los datos guardados en base de datos.

```python title="graficas_descriptivas"
import pandas as pd
import matplotlib.pyplot as plt

# Cargar la base de datos
db_path = 'proyecto.db'  # Asegúrate de que la ruta sea correcta
data = pd.read_sql('SELECT variable_1, variable_2 FROM test_data', 'sqlite:///' + db_path)

# Crear histograma para variable_1
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.hist(data['variable_1'], bins=30, color='blue', alpha=0.7)
plt.title('Histograma de Variable 1')
plt.xlabel('Variable 1')
plt.ylabel('Frecuencia')
plt.xlim(0, 4)  # Limitar el eje X para ver mejor la estructura del histograma

# Crear histograma para variable_2
plt.subplot(1, 2, 2)
plt.hist(data['variable_2'], bins=30, color='orange', alpha=0.7)
plt.title('Histograma de Variable 2')
plt.xlabel('Variable 2')
plt.ylabel('Frecuencia')
plt.xlim(0, 12.5)   # Limitar el eje X para ver mejor la estructura del histograma

# Mostrar gráficas
plt.tight_layout()
plt.show()
```
Ahora bien, al correr este programa se obtienen los resultados que se muestran a continuación.

![Histogramas](img/Histograma_variables.jpeg)

Añadiendo una lógica extra al programa, se puede aproximar los modelos de distribución de mejor ajuste para los histogramas generados. Esto aplicando una normalización de la frecuencia, lo cual se puede observar a continuación.

![Modelos de mejor ajuste](img/Mejor ajuste.jpeg)

Observando la figura anterior se puede deducir que la función de densidad que mejor se ajusta a la variable 1 es de Rayleigh, mientras que, para el caso de la variable 2 es un poco más complicado de ya que parece ser hasta cierto punto constante, pero también exponencial. Dada está incertidumbre, se decide que la función de densidad que mejor se ajusta a la variable 2 es de tipo exponencial.

De forma que, los modelos de probabilidad que mejor se ajustan a las variables 1 y 2 se pueden resumir en la siguiente tabla resumen.


|                  | `variable_1`  | `variable_2`  |
|-------------------------|---------------|---------------|
| **Modelo**               | Rayleigh      | Exponencial      |
