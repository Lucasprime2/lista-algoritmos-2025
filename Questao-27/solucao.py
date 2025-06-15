n = int(input("Quantidade de turmas: "))
while n <= 0:
    n = int(input("Erro: digite uma quantidade de turmas maior que zero: "))
total_alunos = 0
for i in range(1, n + 1):
    alunos = int(input(f"Quantidade de alunos da turma {i}: "))
    while alunos > 40 or alunos <= 0:
        alunos = int(input("Erro: digite um número entre 1 e 40: "))
    total_alunos += alunos
me = total_alunos / n
print(f"Média de alunos por turma: {me:.2f}")