p= float(input("Preço do pão: R$ "))
print("=" * 30)
print("     Panificadora Pão de Ontem")
print("    Tabela de Preços")
print("=" * 30)
for n in range(1, 51):
    t = n * p
    print(f"{n:2d} - R$ {t:.2f}")