n = int(input("Digite o número de termos da série: "))
while n <= 0:
    n = int(input("Erro: digite um número maior que zero: "))
a, b = 1, 1
print("\nSérie de Fibonacci até o termo digitado:")
for i in range(n):
    print(a)
    a, b = b, a + b