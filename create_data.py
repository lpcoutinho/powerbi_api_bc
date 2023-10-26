import pandas as pd
import random
from datetime import datetime, timedelta

# Gerando dados aleatórios
num_rows = 1000

cod_movimentacao = range(1, num_rows+1)
data = [(datetime.today() - timedelta(days=random.randint(0,365))).date() for _ in range(num_rows)]
tipo = random.choices(["Compra", "Venda"], k=num_rows)
classificacao = random.choices(["Eletrônicos", "Vestuário", "Alimentos", "Móveis"], k=num_rows)
documento = [f"NF-{random.randint(1000,9999)}" for _ in range(num_rows)]
centro_custos = random.choices(["Setor de Compras", "Setor de Vendas", "Logística"], k=num_rows)
local = random.choices(["Brasil", "EUA", "China", "Alemanha", "Japão"], k=num_rows)
valor = [random.uniform(50, 5000) for _ in range(num_rows)]
moeda = random.choices(["USD", "EUR", "JPY"], k=num_rows)

# Criando DataFrame
df = pd.DataFrame({
    "Cód de Movimentação": cod_movimentacao,
    "Data": data,
    "Tipo": tipo,
    "Classificação": classificacao,
    "Documento": documento,
    "Centro de Custos": centro_custos,
    "Local": local,
    "Valor": valor,
    "Moeda": moeda
})

# Salvando
df.to_excel("dados_importacao.xlsx", index=False)
# df.to_csv('data.csv', index=False)