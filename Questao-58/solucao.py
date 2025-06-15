dados_originais = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

dados_invertidos = []
for posicao in range(len(dados_originais)-1, -1, -1):
    dados_invertidos.append(dados_originais[posicao])

print("Estrutura original:")
for registro in dados_originais:
    print(registro)

print("\nEstrutura com registros invertidos:")
for registro in dados_invertidos:
    print(registro)