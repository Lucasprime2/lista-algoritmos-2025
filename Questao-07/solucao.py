m = float(input("Digite o 1º número: "))
for i in range(2, 6):
    n = float(input(f"Digite o {i}º número: "))
    if n > m:
        m = n
print(f"\nO maior número digitado é: {m}")