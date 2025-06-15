a = int(input("Digite o primeiro inteiro: "))
b = int(input("Digite o segundo inteiro: "))
i = a
s = 0
while i != b:
    if a < b:
        i += 1
    else:
        i -= 1
    if i != b:
        print(i)
        soma += i
print(f"\na soma é {a} e {b}: {s}")
