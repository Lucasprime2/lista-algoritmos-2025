while True:
    a = int(input("\nNúmero entre 0 e 15: "))
    if not (0 <= a <= 15):
        print("Erro: Use entre 0 e 15.")
        continue
    
    fat = 1
    for i in range(1, a + 1):
        fat *= i
    
    print(f"{a}! = {fat}")
    
    if input("\nQuer calcular novamente? (s/n): ").lower() != 's':
        break