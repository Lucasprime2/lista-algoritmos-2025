qtde_termos = int(input("Digite o número de termos: "))
acumulador = 0.0
num_atual = 1
denom_atual = 1
indice = 1

print("\nElementos da série:")
while indice <= qtde_termos:
    fracao = num_atual / denom_atual
    acumulador += fracao

    if indice == 1:
        print(f"{num_atual}/{denom_atual}", end="")
    else:
        print(f" + {num_atual}/{denom_atual}", end="")

    num_atual += 1
    denom_atual += 2
    indice += 1
print(f"\n\nSoma total da série: {acumulador:.4f}")