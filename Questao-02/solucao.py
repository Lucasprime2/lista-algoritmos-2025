u = input("Digite o nome de usuário: ")
s = input("Digite a senha: ")

while s == u:
    print("A senha não pode ser igual ao nome de usuário. Tente novamente.\n")
    s = input("Digite a senha de novo: ")

print("Cadastro bem sucedido")
print(f"Usuário: {u}")