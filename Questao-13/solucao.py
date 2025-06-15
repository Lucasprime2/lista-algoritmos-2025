a = float(input("base: "))
b = int(input("expoente: "))
resultado = 1
for i in range(abs(b)):
    resultado *= a
if b < 0:
    resultado **= -1
print(f"\n{a} elevado a {b} = {resultado}")
