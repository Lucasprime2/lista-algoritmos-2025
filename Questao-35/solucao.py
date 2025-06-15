n = int(input("Digite um número inteiro: "))
print(f"Números primos entre 1 e {n}:")
for num in range(2, n + 1): 
    primo = True
    for div in range (2,num):
        if num % div == 0:
            primo = False
            break
    if primo:
        print(num, end=' ')