linha = input("Cidade 1 -código, nº de veículos e nº de acidentes (separados por espaço): ").split()
cidade_max = int(linha[0])
cidade_min = cidade_max
veiculos_total = int(linha[1])
acidentes_total = int(linha[2])

maior_qtd_acidentes = acidentes_total
menor_qtd_acidentes = acidentes_total

soma_veiculos = veiculos_total

soma_acidentes_pequenas = 0
cont_cidades_pequenas = 0
if veiculos_total < 2000:
    soma_acidentes_pequenas = acidentes_total
    cont_cidades_pequenas = 1

for num in range(2, 6):
    dados = input(f"Cidade {num} -código, nº de veículos e nº de acidentes: ").split()
    codigo_atual = int(dados[0])
    veiculos_atual = int(dados[1])
    acidentes_atual = int(dados[2])

    if acidentes_atual > maior_qtd_acidentes:
        maior_qtd_acidentes = acidentes_atual
        cidade_max = codigo_atual
    if acidentes_atual < menor_qtd_acidentes:
        menor_qtd_acidentes = acidentes_atual
        cidade_min = codigo_atual

    soma_veiculos += veiculos_atual

    if veiculos_atual < 2000:
        soma_acidentes_pequenas += acidentes_atual
        cont_cidades_pequenas += 1

media_veiculos_geral = soma_veiculos / 5
if cont_cidades_pequenas > 0:
    media_acidentes_pequenas = soma_acidentes_pequenas / cont_cidades_pequenas
else:
    media_acidentes_pequenas = 0

print(f"\nMaior nº de acidentes: {maior_qtd_acidentes} na cidade de código {cidade_max}")
print(f"Menor nº de acidentes: {menor_qtd_acidentes} na cidade de código {cidade_min}")
print(f"Média de veículos nas cinco cidades: {media_veiculos_geral:.2f}")
print(f"Média de acidentes em cidades com <2000 veículos: {media_acidentes_pequenas:.2f}")