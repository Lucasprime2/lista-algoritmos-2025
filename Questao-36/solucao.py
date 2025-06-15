print("Tabuada Personalizada")
n = int(input("Montar a tabuada de: "))
inicio = int(input("Começar por: "))
fim = int(input("Terminar em: "))
if fim < inicio:
    print("\nErro: o valor final é maior que o inicial")
else:
    print(f"\nA tabuada começa em {inicio} e termina em {fim}")
    for i in range(inicio, fim + 1):
        resultado = n * i
        print(f"{n} X {i} = {resultado}")