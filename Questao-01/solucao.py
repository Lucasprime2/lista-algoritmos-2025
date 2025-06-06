while True:
    a = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= a <= 10:
        break
    else:
        print("Valor inválido. Tente de novo.\n")
print(f"A nota é: {a:.1f}.")