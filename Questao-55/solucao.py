dados = [
    [95, 12],
    [7, 83],
    [64, 29],
    [41, 50]
]

valor_maximo = dados[0][0]
valor_minimo = dados[0][0]

for conjunto in dados:
    for numero in conjunto:
        if numero > valor_maximo:
            valor_maximo = numero
        if numero < valor_minimo:
            valor_minimo = numero

print(f"O valor mais alto encontrado: {valor_maximo}")
print(f"O valor mais baixo encontrado: {valor_minimo}")