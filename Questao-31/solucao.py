while True:
    print("Lojas Tabajara")
    t = 0.0
    a= 1
    while True:
        v= float(input(f"Produto {a}: R$ "))
        if v == 0:
            break
        t += v
        a += 1
    print(f"Total: R$ {t:.2f}")
    d = float(input("Dinheiro: R$ "))
    troco = d - t
    print(f"Troco: R$ {troco:.2f}\n")