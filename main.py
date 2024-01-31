import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# Carrega o conjunto de dados do arquivo CSV
arquivo_csv = pd.read_csv("london_weather.csv")

# Converte a coluna 'date' para o formato de data (YYYYMMDD -> datetime)
arquivo_csv['date'] = pd.to_datetime(arquivo_csv['date'], format='%Y%m%d')

# Extrai o ano e o mês da coluna 'date'
arquivo_csv['year'] = arquivo_csv['date'].dt.year
arquivo_csv['month'] = arquivo_csv['date'].dt.month_name()

# Seleciona os anos para comparação
anos_para_comparar = [2019, 2020]

# Filtra os dados para incluir apenas os anos selecionados
anos_selecionados = arquivo_csv[arquivo_csv['year'].isin(anos_para_comparar)]

# Calcula a média de cobertura de nuvens para cada mês e ano
media_nuvens = anos_selecionados.groupby(['year', 'month'])['cloud_cover'].mean().reset_index()

# Plotagem da média de cobertura de nuvens ao longo dos anos
plt.figure(figsize=(14, 8))

for year in anos_para_comparar:
    data_year = media_nuvens[media_nuvens['year'] == year]
    plt.plot(data_year['month'], data_year['cloud_cover'], label=f'Nuvens {year}')

# Configurações do gráfico
plt.title('Comparação de Nuvens ao Longo dos Anos')
plt.xlabel('Mês')
plt.ylabel('Cobertura de Nuvens')
plt.legend()
plt.show()

# Calcula a média de horas de sol para cada mês e ano
media_sol = anos_selecionados.groupby(['year', 'month'])['sunshine'].mean().reset_index()

# Plotagem da média de horas de sol ao longo dos anos
plt.figure(figsize=(14, 8))

for year in anos_para_comparar:
    data_year = media_sol[media_sol['year'] == year]
    plt.plot(data_year['month'], data_year['sunshine'], label=f'Sunshine {year}', marker='o')

# Configurações do gráfico
plt.title('Média de Horas de Sol por Mês')
plt.xlabel('Mês')
plt.ylabel('Horas de Sol')
plt.legend()
plt.tight_layout()  # Ajusta o layout para melhor espaçamento
plt.show()
