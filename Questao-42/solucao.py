contador_0_25 = 0
contador_26_50 = 0
contador_51_75 = 0
contador_76_100 = 0
print("Digite números positivos. Para encerrar digite um número negativo:")
while True:
    numero = float(input())
    if numero < 0: 
        break
    if numero <= 25:
        contador_0_25 += 1
    elif numero <= 50:
        contador_26_50 += 1
    elif numero <= 75:
        contador_51_75 += 1
    elif numero <= 100:
        contador_76_100 += 1
print("\nResultados:")
print(f"[0-25]: {contador_0_25}")
print(f"[26-50]: {contador_26_50}")
print(f"[51-75]: {contador_51_75}")
print(f"[76-100]: {contador_76_100}")