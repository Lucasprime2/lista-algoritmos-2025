n= int(input("Número de eleitores: "))
while n<= 0:
    n= int(input("Erro: digite um número maior que zero: "))
v1 = v2 = v3 = 0
for i in range(1, n + 1):
    print(f"\nEleitor {i}:")
    v = int(input("Vote em 1, 2 ou 3: "))
    while v not in (1, 2, 3):
        v = int(input("Erro: digite 1, 2 ou 3: "))
    if v == 1:
        v1 += 1
    elif v == 2:
        v2 += 1
    else:
        v3 += 1
print("\nQuantidade de votos de cada candidato:")
print(f"Candidato 1: {v1} voto(s)")
print(f"Candidato 2: {v2} voto(s)")
print(f"Candidato 3: {v3} voto(s)")