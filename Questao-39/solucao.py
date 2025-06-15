dados = input("Aluno 1 -número e altura (cm), separados por espaço: ").split()
aluno_alto_id = int(dados[0])
altura_alta = int(dados[1])
aluno_baixo_id = aluno_alto_id
altura_baixa = altura_alta
for contador in range(2, 11):
    valores = input(f"Aluno {contador} -número e altura (cm): ").split()
    aluno_id = int(valores[0])
    altura_atual = int(valores[1])
    if altura_atual > altura_alta:
        altura_alta = altura_atual
        aluno_alto_id = aluno_id
    if altura_atual < altura_baixa:
        altura_baixa = altura_atual
        aluno_baixo_id = aluno_id
print(f"\nAluno mais alto: número {aluno_alto_id} com {altura_alta} cm")
print(f"Aluno mais baixo: número {aluno_baixo_id} com {altura_baixa} cm")