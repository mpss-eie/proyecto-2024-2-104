import pandas as pd
import matplotlib.pyplot as plt

# Cargar la base de datos
db_path = 'proyecto.db'  # Asegúrate de que la ruta sea correcta
data = pd.read_sql('SELECT variable_1, variable_2 FROM test_data', 'sqlite:///' + db_path)

# Crear figura con tamaños ajustados
plt.figure(figsize=(12, 6))

# Crear histograma para variable_1
plt.subplot(1, 2, 1)
plt.hist(data['variable_1'], bins=70, color='dodgerblue', edgecolor='black', alpha=0.75)  # Bins para variable 1 en 70
plt.title('Histograma de Variable 1')
plt.xlabel('Variable 1')
plt.ylabel('Frecuencia')
plt.xlim(0, 4)  # Limitar el eje X para ver mejor la estructura del histograma
plt.grid(True, axis='y', linestyle='--', alpha=0.6)  # Añadir una cuadrícula ligera en el eje Y

# Crear histograma para variable_2 con más bins
plt.subplot(1, 2, 2)
plt.hist(data['variable_2'], bins=100, color='darkorange', edgecolor='black', alpha=0.75)  # Aumentar bins a 100 para variable 2
plt.title('Histograma de Variable 2')
plt.xlabel('Variable 2')
plt.ylabel('Frecuencia')
plt.xlim(0, 12.5)  # Limitar el eje X para ver mejor la estructura del histograma
plt.grid(True, axis='y', linestyle='--', alpha=0.6)  # Añadir una cuadrícula ligera en el eje Y

# Ajustar diseño y mostrar gráficas
plt.tight_layout(pad=3.0)  # Aumentar separación entre gráficas
plt.show()
