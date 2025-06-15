
n = int(input("Quantos CDs você comprou? "))
while n <= 0:
    n= int(input("Erro: digite um número de CDs maior que zero: "))
t = 0.0
for i in range(1, n + 1):
    p = float(input(f"Digite o valor do {i}º CD: R$ "))
    while p< 0:
        p= float(input("Erro: digite um preço não negativo: R$ "))
    t += p
me = t/ n
print(f"\nTotal investido: R$ {t:.2f}")
print(f"Valor médio por CD: R$ {me:.2f}")