import pandas as pd
import matplotlib.pyplot as plt

# Cargar la base de datos
db_path = 'proyecto.db'  # Asegúrate de que la ruta sea correcta
data = pd.read_sql('SELECT variable_1, variable_2 FROM test_data', 'sqlite:///' + db_path);print(variable_1)

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
