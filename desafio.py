x1 = float(input("Digite a coordenada x do primeiro ponto: "))
y1 = float(input("Digite a coordenada y do primeiro ponto: "))
x2 = float(input("Digite a coordenada x do segundo ponto: "))
y2 = float(input("Digite a coordenada y do segundo ponto: "))

distancia = (((x2 - x1)**2) + ((y2 - y1)**2)) ** 0.5
print(f"A distância euclidiana entre os pontos ({x1:.1f}, {y1:.1f}) e ({x2:.1f}, {y2:.1f}) é {distancia:.1f}")