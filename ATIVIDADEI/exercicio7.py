metrificacao = input("Digite 'C' para converter de Celsius para Fahrenheit ou 'F' para converter de Fahrenheit para Celsius: ")
temperatura = float(input("Digite a temperatura: "))

if metrificacao == "C":
    temperatura2 = (temperatura * 1.8) + 32
    print(f"{temperatura:.1f} é equivalente a {temperatura2:.2f}")
elif metrificacao == "F":
    temperatura2 = (temperatura - 32) / 1.8
    print(f"{temperatura:.1f} é equivalente a {temperatura2:.2f}")
else:
    print("não entendi algo, por favor, volte ao começo.")