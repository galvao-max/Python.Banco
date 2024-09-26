#'Desenvolva um programa completo que cadastre alunos:

import os
# Nome do arquivo onde os dados serão armazenados
nome_arquivo = open('cadastro_alunos.txt', 'w', encoding='utf-8')

def cadastrar_aluno():
    nome_arquivo = "cadastro_alunos.txt"  # Defina o nome do arquivo aqui
    """Função para cadastrar um novo aluno."""
    nome = input("Informe o nome do aluno: ")
    email = input("Informe o email do aluno: ")
    curso = input("Informe o curso do aluno: ")
    
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(f"Nome:{nome};\nEmail:{email};\nCurso:{curso}\n")
        
    
    print(f"Aluno {nome} cadastrado com sucesso!\n")

import os
def listar_alunos():
    nome_arquivo = "cadastro_alunos.txt"  # Defina o nome do arquivo aqui
    """Função para listar todos os alunos cadastrados."""
    if not os.path.exists(nome_arquivo):
        print("Nenhum aluno cadastrado ainda.\n")
        return
    
    with open(nome_arquivo, 'r') as arquivo:
        alunos = arquivo.readlines()
    
    if alunos:
        print("Lista de alunos cadastrados:")
        for aluno in alunos:
            nome, email, curso = aluno.strip().split(';')
            print(f"Nome: {nome}, Email: {email}, Curso: {curso}")
           
    else:
        print("Nenhum aluno cadastrado ainda.")
    print()

def buscar_aluno():
    """Função para buscar um aluno pelo nome."""
    nome_busca = input("Informe o nome do aluno que deseja buscar: ").strip().lower()
    
    if not os.path.exists(nome_arquivo):
        print("Nenhum aluno cadastrado ainda.\n")
        return
    
    with open(nome_arquivo, 'r') as arquivo:
        alunos = arquivo.readlines()
    
    encontrado = False
    for aluno in alunos:
         # Verificar se o formato da linha está correto
        dados_aluno = aluno.strip().split(';')
        if len(dados_aluno) == 3:
            nome, email, curso = dados_aluno
        
            if nome.strip().lower() == nome_busca: 
                print(f"Aluno encontrado: Nome: {nome}, Email: {email}, Curso: {curso}\n")
                encontrado = True
                break
    
    
    if not encontrado:
        print(f"Aluno com nome '{nome_busca}' não encontrado.\n")

def menu():
    """Função para exibir o menu de opções."""
    while True:
        print("Sistema de Registro de Alunos")
        print("1. Cadastrar um novo aluno")
        print("2. Listar os alunos cadastrados")
        print("3. Buscar um aluno pelo nome")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            buscar_aluno()
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o programa
menu()
