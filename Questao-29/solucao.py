print("=" * 30)
print("     Lojas Quase Dois")
print("    Tabela de Preços")
print("=" * 30)
preco= 1.99
for n in range(1, 51):
    t= n * preco
    print(f"{n} - R$ {t:.2f}")