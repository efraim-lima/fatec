lista = [10, 20, 30, 40, 30, 20, 60]
i = 0
maior_num = lista[i]

while i <= len(lista):
    j = i + 1
    print(i)
    if lista[j] > lista[i]:
        print(lista[j])
        maior_num = lista[j]
    else:
        pass
    
    i = i + 1
    
print(maior_num)