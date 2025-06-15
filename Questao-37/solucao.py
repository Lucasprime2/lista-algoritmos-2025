total_participantes = 0
soma_alturas = 0.0
soma_pesos = 0.0

codigo_mais_alto = None
altura_mais_alto = None
codigo_mais_baixo = None
altura_mais_baixo = None

codigo_mais_gordo = None
peso_mais_gordo = None
codigo_mais_magro = None
peso_mais_magro = None

while True:
    registro = int(input("Código do cliente (999 para encerrar"))
    if registro == 999:
        break

    altura_atual = float(input("Altura (m): "))
    peso_atual   = float(input("Peso (kg): "))

    total_participantes += 1
    soma_alturas        += altura_atual
    soma_pesos          += peso_atual

    if altura_mais_alto is None or altura_atual > altura_mais_alto:
        altura_mais_alto = altura_atual
        codigo_mais_alto = registro
    if altura_mais_baixo is None or altura_atual < altura_mais_baixo:
        altura_mais_baixo = altura_atual
        codigo_mais_baixo = registro

    if peso_mais_gordo is None or peso_atual > peso_mais_gordo:
        peso_mais_gordo = peso_atual
        codigo_mais_gordo = registro
    if peso_mais_magro is None or peso_atual < peso_mais_magro:
        peso_mais_magro = peso_atual
        codigo_mais_magro = registro

if total_participantes == 0:
    print("Sem cadastro de cliente")
else:
    media_alturas = soma_alturas / total_participantes
    media_pesos   = soma_pesos   / total_participantes

    print(f"\nTotal de clientes: {total_participantes}")
    print(f"Código do mais alto: {codigo_mais_alto} - {altura_mais_alto:.2f} m")
    print(f"Código do mais baixo: {codigo_mais_baixo} - {altura_mais_baixo:.2f} m")
    print(f"Código do mais gordo: {codigo_mais_gordo} - {peso_mais_gordo:.2f} kg")
    print(f"Código do mais magro: {codigo_mais_magro} - {peso_mais_magro:.2f} kg")
    print(f"Média de altura: {media_alturas:.2f} m")
    print(f"Média de peso: {media_pesos:.2f} kg")