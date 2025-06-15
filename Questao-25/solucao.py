n = int(input("Quantidade de pessoas:"))
while n <= 0:
    n = int(input("Erro: digite um valor maior que zero: "))
s = 0
for i in range(1, n + 1):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    s += idade
me = s / n
print(f"\nMédia de idade da turma: {me:.1f} anos")
if me<= 25:
    print("JOVEM")
elif me <= 60:
    print("ADULTA")
else:
    print("IDOSA")