#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

# Solicita ao usuário que insira o raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Calcula a área do círculo usando a fórmula: área = π * raio²
area = math.pi * (raio ** 2)

# Exibe a área do círculo
print(f"A área do círculo com raio {raio} é {area:.2f}.")