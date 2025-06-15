qtd_linhas = int(input("Quantidade de fileiras: "))
qtd_colunas = int(input("Quantidade de colunas: "))

estrutura = []

for indice_i in range(qtd_linhas):
    fileira_nova = []
    
    for indice_j in range(qtd_colunas):
        celula_valor = indice_i * indice_j
        fileira_nova.append(celula_valor)
    estrutura.append(fileira_nova)

print(f"\nEstrutura {qtd_linhas}x{qtd_colunas}:")
for sequencia in estrutura:
    print(sequencia)