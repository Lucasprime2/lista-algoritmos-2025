matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]

transposta = []
for j in range(len(matriz[0])):    
    nova_linha = []                
    for i in range(len(matriz)):   
        nova_linha.append(matriz[i][j])
    transposta.append(nova_linha)

print("Matriz original:")
for linha in matriz:
    print(linha)

print("\nMatriz transposta:")
for linha in transposta:
    print(linha)