n = int(input("Quantidade de notas: "))
while n <= 0:
    n = int(input("Erro: digite um valor maior que zero: "))
s = 0.0
for i in range(1, n + 1):
    nota = float(input(f"Digite a nota: "))
    s += nota
me = s / n
print(f"\nMédia das {n} notas: {me:.2f}")