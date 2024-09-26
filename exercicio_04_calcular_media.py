#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
# Solicita ao usuário que insira as quatro notas bimestrais
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibe a média
print(f"A média das notas é {media:.2f}")