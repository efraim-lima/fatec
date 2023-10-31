comprimento1 = int(input("Digite o  comprimento do primeiro lado: "))
comprimento2 = int(input("Digite o  comprimento do segundo lado: "))
comprimento3 = int(input("Digite o  comprimento do terceiro lado: "))

if comprimento1 == comprimento2 == comprimento3: # duvida: por que a lógica não funcionou quando verifiquei primeiro o isóceles?
    print("O triângulo é equilátero.")
elif comprimento1 == comprimento2 or comprimento1 == comprimento3 or comprimento2 == comprimento3:
    print("O triângulo é isóceles.")
else:
    print("O triângulo é escaleno.")