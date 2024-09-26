
#Função para exibir as opções de cadastro 


def entradaUsuario():
    """Função para exibir as opções de cadastro"""
    global acao  # variável global
    print('''
1: Cadastrar novo aluno.
2: Listar alunos cadastrados.
3: Procurar aluno pelo nome.
4: SAIR.''')
    acao = int(input('O que deseja fazer? '))

# Função para inserir um novo aluno
def cadastraAluno():
    print('Cadastro de aluno. Preencha as informações:')
    # tratamento de strings
    ok = 0  # variável sinalizadora (flag)
    while ok == 0:
        matricula = input('Matrícula: ').strip()
        nome = input('Nome: ').strip()
        email = input('E-mail: ').strip()
        curso = input('Curso: ').strip()

        # (i) Tratar entradas vazias
        if not matricula or not nome or not email or not curso:
            print("Entrada vazia! Redigite.\n")
        else:
            # (ii) Tratar nomes de alunos que contêm números
            if not nome.isalpha():  # isalpha garante que apenas letras estejam no nome
                print("Somente caracteres no nome! Redigite.\n")
            else:
                # (iii) Tratar número de matrículas com caracteres
                if not matricula.isdigit():
                    print("Somente números na matrícula! Redigite.\n")
                else:
                    ok = 1  # tudo certo

    aluno = f'{matricula},{nome},{email},{curso}\n'  # formato
    # (i) Tratar fechamento de arquivos que não foram abertos
    with open('alunos.txt', 'a', encoding='UTF-8') as arquivo:
        arquivo.write(aluno)  # gravar aluno adicionando ao arquivo
    print('Cadastrado!!!\n')

# Função para listar os dados dos alunos
def listaAluno():
    # tratamento de exceções
    try:
        # (ii) tentar escrever em arquivos com permissão para somente leitura
        with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
            listaAlunos = arquivo.read().split('\n')  # ler o registro
            print('\nLista de alunos cadastrados:')
            print('Matrícula, Nome, Email, Curso')
            for aluno in listaAlunos:
                if aluno.strip():  # Ignora linhas vazias
                    print(aluno)
    except FileNotFoundError:
        print('Arquivo não existe. Cadastre primeiro!!!\n')

# Função para buscar um aluno pelo nome
def procuraAluno():
    # tratamento de exceções
    try:
        print('Buscar aluno por nome:')
        busca = input('Nome: ').strip()
        if not busca:
            print('Entrada vazia!!!')
        else:
            with open('alunos.txt', 'r', encoding='utf-8') as arquivo:
                listaAlunos = arquivo.read().split('\n')  # separa os dados
                resultado = None
                for aluno in listaAlunos:
                    if aluno.strip():  # Ignora linhas vazias
                        # divide com , e remove espaço no fim
                        nomeAluno = aluno.split(',')[1].strip()
                        if busca.lower() == nomeAluno.lower():  # Comparação sem case-sensitive
                            resultado = aluno  # encontrou
                            break
                if resultado is None:  # não encontrou
                    print('\nNão foi encontrado nenhum aluno com esse nome.\n')
                else:
                    print(resultado + '\n')
    except FileNotFoundError:
        print('Arquivo não existe. Cadastre primeiro!!!\n')

# Programa principal
# repete até encerrar
while True:
    entradaUsuario()
    if acao == 1:
        cadastraAluno()
    elif acao == 2:
        listaAluno()
    elif acao == 3:
        procuraAluno()
    elif acao == 4:
        print("Encerrando o programa.")
        break
    else:
        print('\n::::: Escolha uma das quatro opções! :::::\n')
# Fim do programa