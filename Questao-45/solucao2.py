print("Gabarito da prova (10 respostas, A-E), separadas por espaço:")
chave_prova = input("Gabarito: ").strip().upper().split()

num_alunos = 0
total_acertos = 0
nota_maxima = -1
nota_minima = 11

while True:
    num_alunos += 1
    acertos_aluno = 0

    print(f"\nAluno #{num_alunos}: responda as 10 questões (A-E).")
    for indice in range(10):
        resposta = input(f"Questão {indice+1}: ").strip().upper()
        if resposta == chave_prova[indice]:
            acertos_aluno += 1

    total_acertos += acertos_aluno
    if acertos_aluno > nota_maxima:
        nota_maxima = acertos_aluno
    if acertos_aluno < nota_minima:
        nota_minima = acertos_aluno

    print(f"Resultado do aluno #{num_alunos}: {acertos_aluno} acerto(s).")
    continuar = input("Registrar outro aluno? (S/N) ").strip().upper()
    if continuar != 'S':
        break

media_turma = total_acertos / num_alunos if num_alunos > 0 else 0

print("\n=== Resultados da turma ===")
print(f"Total de alunos: {num_alunos}")
print(f"Maior acerto: {nota_maxima}")
print(f"Menor acerto: {nota_minima}")
print(f"Média da turma: {media_turma:.2f}")