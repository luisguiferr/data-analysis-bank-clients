import pandas as pd
import os

os.makedirs('data/raw', exist_ok=True)

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'
df = pd.read_csv(url)

df.to_csv('data/raw/clientes_banco.csv', index=False)