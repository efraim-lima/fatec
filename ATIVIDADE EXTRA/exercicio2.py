lista = [1,2,3,4,5,6,7,8,9,10]
lista_inversa = []
i=1

while i <= len(lista):
    lista_inversa.append(lista[-i])
    i += 1
    
print(lista_inversa)