import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
file_path = 'Combined Data.csv'
health = pd.read_csv(file_path)

# Visualizar as primeiras linhas do DataFrame
print(health.head())

print(health['status'].value_counts())

# Contagem de valores únicos em uma coluna específica
status_counts = health['status'].value_counts()

plt.figure(figsize=(10, 6))
status_counts.plot(kind='bar')
plt.title('Distribuição dos Status de Saúde')
plt.xlabel('Status')
plt.ylabel('Contagem')
plt.xticks(rotation=45)
plt.show()


