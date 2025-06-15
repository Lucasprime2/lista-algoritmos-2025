x = int(input("digite o número da tabuada: "))
while x < 1 or x > 10:
    x = int(input("Erro: o número precisa estar entre um e dez: "))
print(f"\nTabuada de {x}:")
for i in range(1, 11):
    print(f"{x} X {i} = {x * i}")