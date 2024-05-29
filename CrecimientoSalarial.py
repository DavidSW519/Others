import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generar semestres desde 2020 hasta 2024
fechas = pd.date_range(start='2021-01-01', end='2024-12-31', freq='6MS')
semestres = [f"{fecha.year}-{'1' if fecha.month == 1 else '2'}" for fecha in fechas]
# Generar salarios aleatorios
np.random.seed(0)  # Para reproducibilidad
salarios = [18,18,19,25,23,27,31,37]

# Crear el DataFrame
df = pd.DataFrame({
    'Semestre': semestres,
    'Salario': salarios
})

# Graficar los datos
plt.figure(figsize=(10, 6))
plt.plot(df['Semestre'], df['Salario'], marker='o')
plt.title('Salarios Semestrales (2020-2024)')
plt.xlabel('Semestre')
plt.ylabel('Salario')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
