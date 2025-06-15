qtde_linhas = int(input("Número de linhas: "))
qtde_colunas = int(input("Número de colunas: "))
valor_busca = int(input("Digite o elemento específico a procurar: "))
total_encontrado = 0

for linha in range(qtde_linhas):
    dados = input(f"Digite os {qtde_colunas} valores da linha {linha+1}, separados por espaço: ").split()
    for dado in dados:
        if int(dado) == valor_busca:
            total_encontrado += 1

print(f"O elemento {valor_busca} aparece {total_encontrado} vez(es) na matriz.")