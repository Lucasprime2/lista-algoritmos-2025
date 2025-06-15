cont_votos_cand1 = cont_votos_cand2 = cont_votos_cand3 = cont_votos_cand4 = 0
cont_votos_nulos = cont_votos_brancos = 0
cont_total_votos = 0

while True:
    voto_codigo = int(input("Digite o código do voto (999 para encerrar): "))
    if voto_codigo == 999:
        break

    cont_total_votos += 1

    if voto_codigo == 1:
        cont_votos_cand1 += 1
    elif voto_codigo == 2:
        cont_votos_cand2 += 1
    elif voto_codigo == 3:
        cont_votos_cand3 += 1
    elif voto_codigo == 4:
        cont_votos_cand4 += 1
    elif voto_codigo == 5:
        cont_votos_nulos += 1
    elif voto_codigo == 6:
        cont_votos_brancos += 1
    else:
        print("Erro: código inválido, o voto não foi guardado.")
        cont_total_votos -= 1  

if cont_total_votos > 0:
    perc_votos_nulos = (cont_votos_nulos / cont_total_votos) * 100
    perc_votos_brancos = (cont_votos_brancos / cont_total_votos) * 100
else:
    perc_votos_nulos = perc_votos_brancos = 0

print(f"\nTotal de votos por candidato:")
print(f"  Candidato A (1): {cont_votos_cand1}")
print(f"  Candidato B (2): {cont_votos_cand2}")
print(f"  Candidato C (3): {cont_votos_cand3}")
print(f"  Candidato D (4): {cont_votos_cand4}")
print(f"Votos nulos (5): {cont_votos_nulos}")
print(f"Votos em branco (6): {cont_votos_brancos}")
print(f"Votos apurados: {cont_total_votos}\n")
print(f"Percentual de votos nulos: {perc_votos_nulos:.2f}%")
print(f"Percentual de votos em branco: {perc_votos_brancos:.2f}%")