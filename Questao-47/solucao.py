while True:
    nome_atleta = input("Atleta (pressione Enter para sair): ").strip()
    if nome_atleta == "":
        break

    avaliacoes = []
    for indice in range(7):
        pontuacao = float(input(f"Nota {indice+1}: "))
        avaliacoes.append(pontuacao)

    print(f"\nAtleta: {nome_atleta}")
    for indice in range(7):
        print(f"Nota {indice+1}: {avaliacoes[indice]:.1f}")

    maior_nota = avaliacoes[0]
    menor_nota = avaliacoes[0]
    soma_notas = 0.0
    for indice in range(7):
        nota_atual = avaliacoes[indice]
        soma_notas += nota_atual
        if nota_atual > maior_nota:
            maior_nota = nota_atual
        if nota_atual < menor_nota:
            menor_nota = nota_atual

    soma_filtrada = soma_notas - maior_nota - menor_nota
    media_apurada = soma_filtrada / 5

    print("\nResultado final:")
    print(f"Atleta: {nome_atleta}")
    print(f"Melhor nota: {maior_nota:.1f}")
    print(f"Pior nota: {menor_nota:.1f}")
    print(f"Média: {media_apurada:.2f}\n")