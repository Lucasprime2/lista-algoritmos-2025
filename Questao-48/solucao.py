a = int(input("Digite um número inteiro positivo: "))
if a < 0:
    print("Erro: digite um número inteiro positivo.")
else:
    original = a
    invertido = 0
    while a > 0:
        digito = a % 10        
        invertido = invertido * 10 + digito  
        a = a // 10            
    print("Original:", original)
    print("Invertido:", invertido)