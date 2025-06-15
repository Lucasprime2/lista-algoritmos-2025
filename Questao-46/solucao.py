while True:
    atleta_nome = input("Atleta (Pressione Enter para sair): ").strip()
    if atleta_nome == "":
        break

    distancias_salto = []
    posicoes_salto = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
    for idx in range(5):
        salto_valor = float(input(f"{posicoes_salto[idx]} Salto (m): "))
        distancias_salto.append(salto_valor)

    print(f"\nAtleta: {atleta_nome}")
    for idx in range(5):
        print(f"{posicoes_salto[idx]} Salto: {distancias_salto[idx]:.1f} m")

    salto_maximo = distancias_salto[0]
    salto_minimo = distancias_salto[0]
    soma_total_saltos = 0.0
    for idx in range(5):
        medida = distancias_salto[idx]

        if medida > salto_maximo:
            salto_maximo = medida
        
        if medida < salto_minimo:
            salto_minimo = medida
    
        soma_total_saltos += medida

    soma_filtrada = soma_total_saltos - salto_maximo - salto_minimo
    media_final = soma_filtrada / 3

    print(f"Melhor salto: {salto_maximo:.1f} m")
    print(f"Pior salto: {salto_minimo:.1f} m")
    print(f"Média dos demais saltos: {media_final:.1f} m")
    print("\nResultado final:")
    print(f"{atleta_nome}: {media_final:.1f} m\n")