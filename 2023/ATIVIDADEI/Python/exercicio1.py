caracter = input("Digite um caractere entre numeros ou letras: ")
vogais = ["a", "e", "i", "o", "u"]
numeros = ["1", "2" , "3", "4", "5", "6", "7", "8", "9", "0"]

if caracter in vogais:
    print("O caractere digitado é uma vogal")
elif caracter in numeros:
    print("O caractere digitado é um número")
else:
    print("O caractere digitado é uma consoante")