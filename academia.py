import sqlite3 as conector

# Função para criar a tabela caso não exista
def criar_tabela():
    conexao = conector.connect('academia.db')
    cursor = conexao.cursor()

    # Criar a tabela, se não existir
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cadastro (
        codigo INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL
    )
    ''')

    # Efetivação do comando
    conexao.commit()
    cursor.close()
    conexao.close()

# Função para inserir registros
def inserir_aluno(codigo, nome, idade):
    conexao = conector.connect('academia.db')
    cursor = conexao.cursor()

    sql = 'INSERT INTO cadastro (codigo, nome, idade) VALUES (?, ?, ?)'
    cursor.execute(sql, (codigo, nome, idade))

    conexao.commit()
    cursor.close()
    conexao.close()

# Função para listar todos os registros
def listar_alunos():
    conexao = conector.connect('academia.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM cadastro')
    alunos = cursor.fetchall()

    if alunos:
        for aluno in alunos:
            print(f"Código: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}")
    else:
        print("Nenhum aluno cadastrado.")

    cursor.close()
    conexao.close()

# Função para atualizar um registro
def atualizar_aluno(codigo, nome=None, idade=None):
    conexao = conector.connect('academia.db')
    cursor = conexao.cursor()

    # Atualizar nome e idade se fornecidos
    if nome and idade:
        sql = 'UPDATE cadastro SET nome = ?, idade = ? WHERE codigo = ?'
        cursor.execute(sql, (nome, idade, codigo))
    elif nome:
        sql = 'UPDATE cadastro SET nome = ? WHERE codigo = ?'
        cursor.execute(sql, (nome, codigo))
    elif idade:
        sql = 'UPDATE cadastro SET idade = ? WHERE codigo = ?'
        cursor.execute(sql, (idade, codigo))
    
    conexao.commit()
    cursor.close()
    conexao.close()

# Função para deletar um registro
def deletar_aluno(codigo):
    conexao = conector.connect('academia.db')
    cursor = conexao.cursor()

    sql = 'DELETE FROM cadastro WHERE codigo = ?'
    cursor.execute(sql, (codigo,))

    conexao.commit()
    cursor.close()
    conexao.close()

# Testando o CRUD
if __name__ == '__main__':
    criar_tabela()  # Criar a tabela se não existir

    # Inserir alunos
    inserir_aluno(1286, 'Rodrigo Silva', 44)
    inserir_aluno(1376, 'Marcus Saraiva', 24)

    # Listar alunos cadastrados
    print("Alunos cadastrados:")
    listar_alunos()

    # Atualizar aluno
    atualizar_aluno(1286, nome="Rodrigo Souza", idade=45)

    # Listar alunos após atualização
    print("\nAlunos após atualização:")
    listar_alunos()

    # Deletar aluno
    deletar_aluno(1376)

    # Listar alunos após deleção
    print("\nAlunos após deleção:")
    listar_alunos()

    print("Fim do programa")