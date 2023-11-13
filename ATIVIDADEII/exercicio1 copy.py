senha = "123"
tentativas = 0
limite = 3

while tentativas < limite:
    senha_input = input("Digite a senha: ")
   
    if senha_input != senha:
        print("Senha incorreta. Tente novamente")
        tentativas += 1
        continue
    else:
        print("Senha correta, login efetivado!")
        break

if tentativas == 3:
    print("Você esgotou suas tentativas. Acesso negado.")