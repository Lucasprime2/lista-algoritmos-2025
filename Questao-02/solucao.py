u = input("Digite o nome de usuário: ")
s = input("Digite a senha: ")

while s == u:
    print("A senha e o nome de usuário não podem ser iguais. Tente novamente.\n")
    s = input("Digite a senha de novo: ")

print("Cadastro bem sucedido")
print(f"Usuário: {u}")