a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
i = a
while i != b:
    if a < b:
        i += 1
    else:
        i -= 1
    if i != b:
        print(i)