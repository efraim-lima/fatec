#Esta seria uma solução mais simples:
senha = "123"
tentativas = 0

while tentativas < 3:
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
    
    


#Aqui seria uma solução que eu adotaria, tomando liberdade de adicionar algumas funcionalidades
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