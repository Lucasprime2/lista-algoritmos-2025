s= 1000.0
t = 1.5
s *= 1 + t/100
for n in range(1997,2026):
    t *= 2                     
    s *= 1 + t/100
print(f"Salário em 2025: R$ {s:.2f}")


salario = float(input("Salário inicial em 1995: R$ "))
taxa = 1.5
salario *= 1 + taxa/100
for i in range (1997,2026):
    taxa *= 2
    salario *= 1 + taxa/100
print(f"Salário em 2025: R$ {salario:.2f}")