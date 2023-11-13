senha = "123"
tentativas = 0
limite = 3

while tentativas < limite:
    senha_input = input("Digite a senha: ")
   
    if senha_input != senha:
        print("Senha incorreta.") #Fiz uma alteração no texto, pois não faria sentido aparecer "Tente novamente" na ultima tentativa
        tentativas += 1
        if tentativas < limite: #Adicionei este contador de tentativas para ficar mais interativo
            print(f"Restam {limite - tentativas} tentativas para seu acesso ser negado")
        continue
    else:
        print("Senha correta, login efetivado!")
        break

if tentativas == limite:
    print("Você esgotou suas tentativas. Acesso negado.")