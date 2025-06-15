n = int(input("Digite um número inteiro positivo n: "))
if n <= 0:
    print("Por favor, informe um valor maior que zero.")
else:
    H = 0.0
    contador = 1
    while contador <= n:
        H += 1 / contador
        contador +=  1
print("O valor de H para n =", n, "é", round(H, 6))