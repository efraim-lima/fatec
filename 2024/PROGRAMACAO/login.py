from hashlib import sha256

loginOk = "ABC"
senhaOk = "abc123"
loginI = ""
senhaI = ""
i = 0
tentativas = 3

while i<=tentativas:
    loginI = input("Digite seu Login: ")
    senhaI = input("Digite sua senha: ")
    senha_hash = sha256(senhaI.encode('utf-8')).hexdigest()
    print(senha_hash)
    
    if i == (tentativas - 1):
        print("\n Esta é  a ultima tentativa \n")

    if loginI == loginOk and senhaI == senhaOk:
        print("Acesso concedido")
        break
    elif i < tentativas:
        print("Tente novamente")
        print(f"Voce possui {tentativas - i} tentativa(s)")
        print(i)
        print(tentativas - 1)
        i+=1
    elif i == 2:
        print("ACABOU!")
    else:
        print("Acesso negado")
        break
