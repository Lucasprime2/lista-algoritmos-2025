N = int(input("Qual o tamanho do conjunto?: "))
while N <= 0:
    N = int(input("Erro: digite um valor maior que zero: "))
n = float(input("Digite o primeiro número: "))
while n < 0 or n > 1000:
    n = float(input("Erro: digite um valor entre 0 e 1000: "))
m = ma = s = n
for i in range(2, N + 1):
    n = float(input(f"Digite o número {i}: "))
    while n < 0 or n> 1000:
        n = float(input("Erro: digite um valor entre 0 e 1000: "))
    s += n
    if n< m:
        m = n
    if n> ma:
        ma = n
print(f"\nMenor valor: {m}")
print(f"Maior valor: {ma}")
print(f"Soma dos valores: {s}")