n = int(input("digite um número inteiro:"))
s = ""
fatorial = 1
for i in range(n, 0, -1):
    s += str(i)
    fatorial *= i
    if i > 1:
        s += " . "
print(f"{n}! = {s} = {fatorial}")