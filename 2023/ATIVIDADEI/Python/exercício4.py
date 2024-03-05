numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))


if numero1 > numero2 > numero3:
    print(f"O maior número é {float(numero1)}")
elif numero2 > numero1 > numero3:
    print(f"O maior número é {float(numero2)}")
else:
    print(f"O maior número é {float(numero3)}")