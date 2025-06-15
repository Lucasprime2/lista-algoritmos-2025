a = int(input("Digite um número inteiro positivo: "))
while a < 0:
    a = int(input("Erro: digite um inteiro positivo: "))
fatorial = 1
for i in range(2, a + 1):
    fatorial *= i
print(f"\n{a}! = {fatorial}")