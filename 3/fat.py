import json

# abre o arquivo json com os dados de faturamento
with open('faturamento.json') as f:
    faturamento_diario = json.load(f)

# cria uma lista com o faturamento de cada dia do mês
faturamento = list(faturamento_diario.values())

# calcula o menor valor de faturamento
menor_faturamento = min(faturamento)

# calcula o maior valor de faturamento
maior_faturamento = max(faturamento)

# calcula a média mensal de faturamento, ignorando os dias com faturamento igual a zero
dias_com_faturamento = [f for f in faturamento if f > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# conta o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for f in dias_com_faturamento if f > media_mensal)

# exibe os resultados
print("Menor faturamento: R$", menor_faturamento)
print("Maior faturamento: R$", maior_faturamento)
print("Dias com faturamento acima da média: ", dias_acima_da_media)