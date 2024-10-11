# Avance Proyecto de programación 

**Integrantes del grupo**

1. Denzel Darío Guzmán Carranza
2. Josué García Blandón

En esta documentación se observará la exploración de los datos realizada 
tras su recopilación.

Dentro de la base de datos llamada como proyecto.db se guardan los datos recopilados
y, aprovechando las herramientas de programación de python se definirán los aspectos
escenciales de la distribución de probabilidad que conforman las variables 1 y 2.

## Definiciones importantes

!!! note "Función de distribución de probabilidad"
    La función de densidad de probabilidad se define como la probabilidad
    según la cual una variable aleatoria puede adquirir un valor determinado 

!!! note "Histograma"
    Un histograma se define brevemente como una forma de representación gráfica
    de la recurrencia con la que sucede un determinado evento. Sirve para simbolizar
    la distribución de un conjunto de datos.

### Tipos de modelos de distribución de probabilidad

1. Distribución normal
2. Exponencial
3. Rayleigh
4. Uniforme
5. Bernoulli
6. Boltzmann

Y muchos otros modelos de distribución, tantos que no sería recomendable agregarlos
todos a la lista.

### Pasos realizados para la recopilación de *datos*

1. Importantísimo siempre activar el ambiente de python antes de realizar cualquier acción. 
2. En tres terminales separadas activar redis-server, celery tasks y celery beat con el fin de iniciar la toma de datos.
3. Eliminar la variable 3 del código del repositorio ya que esta no está contemplada en el funcionamiento regular.
4. Una vez el código esté trabajando consistentemente, dejarlo activo en segundo plano durante al menos 12 horas seguidas.
5. Asegurarse de que los datos se estén actualizando con cada ciclo y que el número de datos aumente de forma gradual a medida que pasan las horas.

### Repositorio remoto y github
Para la realización de este proyecto es sumamente importante mantener un contacto ordenado y coordinado con los miembros del grupo. Es por ello que la plataforma github es sumamente útil para mejorar la coordinación y agilizar el trabajo.

