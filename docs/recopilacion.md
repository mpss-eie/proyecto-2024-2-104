# Recopilación y almacenamiento de datos

En este apartado se documentará cómo se recopilaron los datos y se explorarán los programas `.py`diseñados para la creación de gráficas e histogramas. A continuación se explicarán las librerías utilizadas para confeccionar la lógica de programación para los programas creados externos a los brindados en el repositorio

### **1. Pandas**

Pandas es una librería de python que facilita la manipulación y el análisis de datos. Proporciona herramientas que facilita el trabajo con tablas de datos.

Enfocado a aspectos del proyecto, pandas permite seleccionar y filtrar, a través de comandos y de forma sencilla los conjuntos de datos que me interesan de una tabla. Por ejemplo los datos de la primera columna o de la segunda según sea el caso.


### Gráficas descriptivas de las varbales 1 y 2

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

Aquí fueron creadas las tres tablas, donde `matriculas` hace referencia por medio de llaves foráneas a las llaves primarias `estudiantes.estudiante_id` y `cursos.curso_id`. En esta misma tabla nótese también que las tres columnas tienen `primary_key=True`, lo que indica una *llave primaria compuesta*, para lo cual cada registro debe tener una *combinación única* de estudiante, curso y ciclo lectivo.

Finalmente, hay que crear las tablas estableciendo un `engine` o referencia a la base de datos a utilizar (en este caso SQLite3) y crear una *sesión* ligada a ese `engine`, para poder ejectuar las transacciones deseadas.

```python
# Crear la conexión a la base de datos SQLite3
engine = create_engine(f"sqlite:///{name}")
Session = sessionmaker(bind=engine)
session = Session()

# Crear la(s) tabla(s) en la base de datos
Base.metadata.create_all(engine)
```

En este proyecto no está determinado un mecanismo fundamental de *migraciones*, que son necesarias para el caso, completamente usual, en el que hay que realizar una actualización en la base de datos cuando hay cambios en los modelos (*clases*), conservando al mismo tiempo los datos ya almacenados. Por ejemplo, para cambiar el tipo de dato de `estudiante_id` de `String` a `Integer` hay que hacer una migración. [Alembic](https://alembic.sqlalchemy.org/en/latest/) es la forma de hacerlo con SQLAlchemy, pero no está dentro de los alcances del proyecto.

Para el proyecto la recomendación es utilizar SQLite o PostgreSQL. Una diferencia básica entre ambos es que SQLite3 existe como un archivo binario (por ejemplo, `db.sqlite3` o `data.db`) mientras que PostgreSQL es un programa propiamente, instalado en la computadora o servidor. Para proyectos de gran escala PostgreSQL es recomendado, sin embargo SQLite3 tiene capacidad para manejar cientos de millones de datos, así que en nuestro proyecto no es un problema. Quizá hay que tener más cuidado de no borrar el archivo "de un dedazo".
