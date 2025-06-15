popA = float(input("População de A: "))
while popA <= 0:
    popA = float(input("Erro: população de A deve ser > 0: "))

popB = float(input("População de B: "))
while popB <= 0:
    popB = float(input("Erro: população de B deve ser > 0: "))

x = float(input("Taxa anual de A em porcentagem: "))
while x <= 0:
    x = float(input("Erro: taxa de A deve ser > 0: "))
x = 1 + x/100

y = float(input("Taxa anual de B em porcentagem: "))
while y <= 0:
    y = float(input("Erro: taxa de B deve ser > 0: "))
y = 1 + y/100

anos = 0
while popA < popB:
    popA *= x
    popB *= y
    anos += 1

print(f"\nSerão necessários {anos} anos para que A ultrapasse ou seja igual a B.")
print(f"População de A ao final: {int(popA)}")
print(f"População de B ao final: {int(popB)}")