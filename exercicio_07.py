
#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

lado = float(input("Digite o comprimento do lado do quadrado: "))

# Calcula a área do quadrado usando a fórmula: área = lado²
area = lado ** 2

# Calcula o dobro da área
dobro_area = area * 2

# Exibe o dobro da área do quadrado
print(f"A área do quadrado é {area:.2f}. O dobro da área é {dobro_area:.2f}.")