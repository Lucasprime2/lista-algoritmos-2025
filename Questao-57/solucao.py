dados = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

colunas_consistentes = True
qtd_colunas_ref = len(dados[0]) if dados else 0

for registro in dados:
    if len(registro) != qtd_colunas_ref:
        colunas_consistentes = False
        break

eh_quadrada = colunas_consistentes and (len(dados) == qtd_colunas_ref)

print("Todas as linhas têm mesmo número de colunas?", colunas_consistentes)
print("É matriz quadrada?", eh_quadrada)