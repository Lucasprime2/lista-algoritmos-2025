entrada = input("Digite uma frase: ").lower()
total_vogais = 0
total_consoantes = 0
for caractere in entrada:
    if 'a' <= caractere <= 'z': 
        if caractere in 'aeiou':
            total_vogais += 1
        else:
            total_consoantes += 1

print(f"Vogais: {total_vogais}")
print(f"Consoantes: {total_consoantes}")