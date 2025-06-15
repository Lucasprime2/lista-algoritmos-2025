valor_inicial = float(input("Valor da dívida: R$ "))
print("\nValor da Dívida | Valor dos Juros | Quantidade de Parcelas | Valor da Parcela")
print("-----------------------------------------------------------------------------")
for quantidade_parcelas, percentual_juros in [(1, 0), (3, 10), (6, 15), (9, 20), (12, 25)]:
    juros_reais = valor_inicial * percentual_juros / 100
    total_com_juros = valor_inicial + juros_reais
    valor_parcela = total_com_juros / quantidade_parcelas
    
    print(f"R$ {total_com_juros:9.2f} | R$ {juros_reais:9.2f} | {quantidade_parcelas:2} | R$ {valor_parcela:9.2f}")