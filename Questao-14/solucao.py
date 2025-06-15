par = 0
imp = 0
a = 1
while a <= 10:
    x = int(input(f"Digite o {a}º número: "))
    if x % 2 == 0:
        par += 1
    else:
        imp += 1
    a += 1
print(f"\nPares: {par}")
print(f"Ímpares: {imp}")
