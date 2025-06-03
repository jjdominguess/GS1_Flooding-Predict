import pandas as pd
import os

# Caminhos
INPUT_PATH = '../data/raw/dados_enchente.csv'
OUTPUT_PATH = '../data/processed/arquivo_pronto.csv'

# Criar pasta processed se não existir
os.makedirs('../data/processed', exist_ok=True)

# Carregar dados
df = pd.read_csv(INPUT_PATH)

# Converter colunas para tipo correto (garantia extra)
df['Data'] = pd.to_datetime(df['Data'])
df['Chuva_mm'] = pd.to_numeric(df['Chuva_mm'], errors='coerce')
df['Umidade_%'] = pd.to_numeric(df['Umidade_%'], errors='coerce')
df['Temperatura_C'] = pd.to_numeric(df['Temperatura_C'], errors='coerce')
df['Nivel_rio_m'] = pd.to_numeric(df['Nivel_rio_m'], errors='coerce')

# Verificar e remover dados ausentes
print(f"Linhas antes da limpeza: {len(df)}")
df = df.dropna()
print(f"Linhas após limpeza: {len(df)}")

# Salvar dados prontos
df.to_csv(OUTPUT_PATH, index=False)
print(f"Arquivo limpo salvo em: {OUTPUT_PATH}")
