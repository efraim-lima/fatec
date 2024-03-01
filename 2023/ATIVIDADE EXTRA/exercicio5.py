lista = [1,2,3,4,5,6,7,8,9,9.3, 9.2, 10]
maiores_que_6 = []
maior = lista[0]
menor = lista[0]

for i in lista:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    elif i > 6:
        maiores_que_6.append(i)
    
media = sum(lista) / len(lista)
    
print(f"A maior nota é: {maior}")
print(f"A menor nota é {menor}")
print(f"A lista de notas maiores que 6 é: {maiores_que_6}")
print(f"A soma das notas é: {sum(lista)}")
print(f"A quantidade de notas na lista é: {len(lista)}")
print(f"A média das notas é {media}")