
#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


ganho_por_hora = float(input("Digite quanto você ganha por hora: "))


horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

# Calcula o salário total
salario_total = ganho_por_hora * horas_trabalhadas

# Exibe o salário total
print(f"O seu salário total no mês é R$ {salario_total:.2f}.")
