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
    
    


"""
Aqui seria uma solução que eu adotaria 
Tomando liberdade de adicionar algumas funcionalidades, tais como:
- criar uma variável de limite que auxiliaria em integrações futuras,
mas neste código está ajudando apenas a calcular a quantidade tentativas;
- ajustei o texto da senha incorreta para ficar mais coerente com o 
contexto onde ele aparecerá;
- inseri uma outra lógica condicional para printar a quantidade de tentativas restante.

Outros pontos que poderia usar para deixar ainda mais interativo, mas evitei por não serem
coerentes com a proposta do exercício:
- criar funções para o processo, dividindo-as entre:
    -- calcular tentativas e limite de tentativas;
    -- verificar se a senha realmente bate utilizando hashlib;
    -- possibilitar o reset da senha através de outra condição;

"""
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