N = int(input("Digite a quantidade de elementos do conjunto: "))
while N <= 0:
    N = int(input("Erro: digite um valor maior que zero: "))
    i = 1
n = float(input(f"Digite o número {i}: "))
while n < 0 or n > 1000: 
    n = float(input(f"Erro: digite um número entre 0 e 1000 para o número {i}: "))
    me = m = s = n
while i < N:
    i += 1
    n = float(input(f"Digite o número {i}: "))
    while n < 0 or n > 1000:
        n = float(input(f"Erro: digite um número entre 0 e 1000 para o número {i}: "))
    s += n
    if n < me:
        me = n
    if n > m:
        m = n
print(f"\nMenor valor: {me}")
print(f"Maior valor: {m}")
print(f"Soma dos valores do conjunto: {s}")