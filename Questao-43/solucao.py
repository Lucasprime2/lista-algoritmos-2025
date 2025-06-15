soma_total = 0.0

print("Digite o código e a quantidade desejada (separados por espaço).")
print("Use o código 999 para fechar o pedido.\n")

while True:
    dados_entrada = input("Código e quantidade: ").split()
    item_cod = int(dados_entrada[0])
    item_qtd = int(dados_entrada[1])

    if item_cod == 999:
        break

    if item_cod == 100:
        valor_unitario = 1.20
    elif item_cod == 101:
        valor_unitario = 1.30
    elif item_cod == 102:
        valor_unitario = 1.50
    elif item_cod == 103:
        valor_unitario = 1.20
    elif item_cod == 104:
        valor_unitario = 1.30
    elif item_cod == 105:
        valor_unitario = 1.00
    else:
        print("Erro: código inválido, tente de novo.")
        continue

    subtotal = valor_unitario * item_qtd
    soma_total += subtotal
    print(f"Item {item_cod}: {item_qtd} x R$ {valor_unitario:.2f} = R$ {subtotal:.2f}\n")
print(f"Total a pagar: R$ {soma_total:.2f}")