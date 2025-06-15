a = int(input("Digite um número inteiro: "))
if a < 2:
    print(f"{a} não é um número primo.")
else:
    numero_primo = True
    for n in range(2, a):
        if a % n == 0:
            numero_primo = False
            break
    if numero_primo:
        print(f"{a} é primo")
    else:
        print(f"{a} não é primo")