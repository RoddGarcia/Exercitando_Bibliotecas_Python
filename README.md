**Documentação do Código - Análise Climática de Londres**

![london-weather](link-para-uma-imagem-relacionada-ao-clima-de-londres)

Este repositório contém um script Python para análise e visualização da média de cobertura de nuvens e horas de sol em Londres durante os anos de 2019 e 2020. O conjunto de dados utilizado é proveniente do arquivo `london_weather.csv`.

### Pré-requisitos

Antes de executar o script, certifique-se de ter as seguintes bibliotecas instaladas:

```bash
pip install pandas matplotlib numpy
```

### Funcionalidades

#### 1. Carregamento do Conjunto de Dados

O script utiliza a biblioteca Pandas para carregar o arquivo CSV contendo dados climáticos de Londres.

```python
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

arquivo_csv = pd.read_csv("london_weather.csv")
```

#### 2. Conversão da Coluna 'date' para o Formato de Data

A coluna 'date', inicialmente no formato 'YYYYMMDD', é convertida para o formato de data (datetime) para facilitar manipulações subsequentes.

```python
arquivo_csv['date'] = pd.to_datetime(arquivo_csv['date'], format='%Y%m%d')
```

#### 3. Extração do Ano e Mês

São criadas colunas adicionais para armazenar informações separadas de ano e mês, facilitando a análise por períodos.

```python
arquivo_csv['year'] = arquivo_csv['date'].dt.year
arquivo_csv['month'] = arquivo_csv['date'].dt.month_name()
```

#### 4. Seleção dos Anos de Interesse

Os dados são filtrados para incluir somente os anos especificados para comparação (2019 e 2020).

```python
anos_para_comparar = [2019, 2020]
anos_selecionados = arquivo_csv[arquivo_csv['year'].isin(anos_para_comparar)]
```

#### 5. Análise e Visualização da Média de Cobertura de Nuvens

O script realiza o cálculo da média de cobertura de nuvens para cada mês e ano, seguido pela visualização comparativa ao longo dos anos.

```python
media_nuvens = anos_selecionados.groupby(['year', 'month'])['cloud_cover'].mean().reset_index()

plt.figure(figsize=(14, 8))
for year in anos_para_comparar:
    data_year = media_nuvens[media_nuvens['year'] == year]
    plt.plot(data_year['month'], data_year['cloud_cover'], label=f'Nuvens {year}')

plt.title('Comparação de Nuvens ao Longo dos Anos')
plt.xlabel('Mês')
plt.ylabel('Cobertura de Nuvens')
plt.legend()
plt.show()
```

#### 6. Análise e Visualização da Média de Horas de Sol

Da mesma forma, o script realiza o cálculo da média de horas de sol para cada mês e ano, seguido pela visualização comparativa ao longo dos anos.

```python
media_sol = anos_selecionados.groupby(['year', 'month'])['sunshine'].mean().reset_index()

plt.figure(figsize=(14, 8))
for year in anos_para_comparar:
    data_year = media_sol[media_sol['year'] == year]
    plt.plot(data_year['month'], data_year['sunshine'], label=f'Sunshine {year}', marker='o')

plt.title('Média de Horas de Sol por Mês')
plt.xlabel('Mês')
plt.ylabel('Horas de Sol')
plt.legend()
plt.tight_layout()  # Ajusta o layout para melhor espaçamento
plt.show()
```

### Como Executar

Para executar o script, certifique-se de ter o Python instalado e execute o seguinte comando:

```bash
python nome_do_script.py
```

### Contribuições

Contribuições e sugestões são bem-vindas! Caso encontre algum problema ou queira adicionar uma nova funcionalidade, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

### Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.
