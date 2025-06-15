entrada_usuario = input("Digite uma frase: ")
resultado_invertido = ""
contador = len(entrada_usuario) - 1
while contador >= 0:
    resultado_invertido += entrada_usuario[contador]
    contador -= 1
print("Frase invertida:", resultado_invertido)