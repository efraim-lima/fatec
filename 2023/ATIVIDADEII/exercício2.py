lista = []

while True:
    palavra = input("Digite uma palavra ou 'S' para sair: ")
    
    if palavra.upper() == "S":
        break
    
    lista.append(palavra)

print(f"Você digitou a lista {lista}, com tamanho {len(lista)}")

# Uma saída mais amigável para o usuário ler o texto:
lista2 = ', '.join(lista)
print(f"Você digitou as palavras {lista2}, com tamanho {len(lista)}")