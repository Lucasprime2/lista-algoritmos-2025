n = input("Nome: ")
while len(n) <= 3:
    n = input("Erro: nome não pode ser menor ou igual 3 letras. Digite novamente: ")

id = int(input("Idade: "))
while not (0 <= id <= 150):
    id = int(input("Erro: Idade deve ser entre 0 e 150. Digite novamente: "))


s = float(input("Salário: "))
while s <= 0:
    s = float(input("Erro: Salário deve ser maior que zero. Digite novamente: "))

sx = input("Sexo (f/m): ")
while sx not in ("f", "m"):
    sx = input("Erro: Digite 'f' ou 'm': ")

e = input("Estado civil (s/c/v/d): ")
while e not in ("s", "c", "v", "d"):
    e = input("Erro: Digite 's', 'c', 'v' ou 'd': ")

print("\nDados válidos:")
print("Nome:", n)
print("Idade:", id)
print("Salário:", s)
print("Sexo:", sx)
print("Estado civil:", e)