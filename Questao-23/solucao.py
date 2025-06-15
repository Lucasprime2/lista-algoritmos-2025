a = int(input("Mostre primos até: "))
while a < 2:
    a = int(input("Erro: digite um inteiro: "))
div = 0
d = []
for n in range(2, a + 1):
    primo = True
    for j in range(2, n):         
        div += 1            
        if n % j == 0:
            primo = False
            break                
    if primo:
        d.append(n)
print(f"\nPrimos de 1 até {a}:")
print(d)
print(f"\nTotal de divisões: {div}")