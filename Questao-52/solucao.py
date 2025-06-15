ordem = int(input("Digite a ordem da matriz (n): "))
grelha = []
for indice in range(ordem):
    entrada_linha = input(f"Digite os {ordem} elementos da linha {indice+1}, separados por espaço: ").split()
    valores_linha = []
    for item in entrada_linha:
        valores_linha.append(int(item))
    grelha.append(valores_linha)

soma_diag_principal = 0
soma_diag_secundaria = 0

for indice in range(ordem):
    soma_diag_principal += grelha[indice][indice]
    soma_diag_secundaria += grelha[indice][ordem-1-indice]

print("Soma da diagonal principal:", soma_diag_principal)
print("Soma da diagonal secundária:", soma_diag_secundaria)