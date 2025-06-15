a = int(input("Digite um número inteiro: "))
while a < 2:
    a = int(input("Erro: digite um inteiro maior ou igual a 2: "))
d = []
i = 2
l = a // 2
while i <= l:
    if a % i == 0:
        d.append(i)
    i += 1
if not d:
    print(f"\n{a} é primo")
else:
    print(f"\n{a} não é primo")
    print("É divisível por:", *d)