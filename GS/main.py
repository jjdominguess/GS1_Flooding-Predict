import pandas as pd
import numpy as np
import os

# Simulando dados climáticos
np.random.seed(42)
n = 1000

df = pd.DataFrame({
    'Data': pd.date_range(start='2023-01-01', periods=n, freq='D'),
    'Chuva_mm': np.random.gamma(shape=2, scale=15, size=n),       # simula chuva
    'Umidade_%': np.random.uniform(40, 100, size=n),
    'Temperatura_C': np.random.uniform(15, 35, size=n),
    'Nivel_rio_m': np.random.normal(loc=2, scale=0.5, size=n)      # simula nível do rio
})

# Criando variável-alvo: enchente = 1 se Chuva > 50 mm ou Nível do rio > 3.5 m
df['enchente'] = np.where((df['Chuva_mm'] > 50) | (df['Nivel_rio_m'] > 3.5), 1, 0)

# Criar diretório se não existir
os.makedirs('data/raw', exist_ok=True)

# Salvar CSV
df.to_csv('data/raw/dados_enchente.csv', index=False)
print("Arquivo salvo em: data/raw/dados_enchente.csv")
