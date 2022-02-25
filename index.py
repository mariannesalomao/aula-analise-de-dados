import pandas as pd

# from google.colab import files
# uploaded = files.upload()

tabela = pd.read_excel("Vendas.xlsx")

# display(tabela)

idLoja = tabela["ID Loja"]

# display(idLoja)

# Pegar a soma do faturamento total de vendas

faturamento_total = tabela["Valor Final"].sum()
print(faturamento_total)

# Pegar faturamento por loja

faturamento_por_loja = tabela[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()

# display(faturamento_por_loja)

# Fazer análise de faturamento de produto por loja

faturamento_por_produto = tabela[["ID Loja", "Produto", "Valor Final"]].groupby(["ID Loja", "Produto"]).sum()

# display(faturamento_por_produto)
