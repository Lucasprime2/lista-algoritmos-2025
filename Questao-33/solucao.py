print("Departamento de Meteorologia")
print("Digite as temperaturas (digite 999 para encerrar):")
s= 0
cont = 0
a=-1000 
b= 1000  
while True:
    temp = float(input())
    if temp == 999:
        break
    s += temp
    cont += 1
    if temp > a:
        a= temp
        if temp < b:
         b= temp
if cont > 0:
    media = s / cont
    print(f"\nMaior: {a:.1f°C}")
    print(f"Menor: {b:.1f°C}")
    print(f"Média: {media:.1f}°C")
else:
    print("\nInforme uma temperatura")