nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

# notas = [nota1, nota2, nota3] # versão que eu adotaria no dia a dia
# media = sum(notas) / len(notas) # versão que eu adotaria no dia a dia

notas = nota1 + nota2 + nota3 # versão mais coerente com a proposta do material
media = notas / 3 # versão mais coerente com a proposta do material

if media >= 7:
    print(f"Média: {media:.2f}. Aluno aprovado.")
else:
    print(f"Média: {media:.2f}. Aluno não aprovado.")