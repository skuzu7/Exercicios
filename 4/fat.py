faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# calcula o faturamento total
faturamento_total = sum(faturamento_estados.values())

# calcula o percentual de representação de cada estado
percentual_estados = {}
for estado, faturamento in faturamento_estados.items():
    percentual = (faturamento / faturamento_total) * 100
    percentual_estados[estado] = percentual

# exibe os resultados
for estado, percentual in percentual_estados.items():
    print(f"{estado}: {percentual:.2f}%")