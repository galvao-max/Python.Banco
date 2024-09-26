import sqlite3 as conector

# Função para criar as tabelas no banco de dados
def criar_tabelas():
    try:
        conexao = conector.connect('registro_notas.db')
        cursor = conexao.cursor()

        sql1 = '''CREATE TABLE IF NOT EXISTS tbaluno (
                    matricula INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    curso TEXT NOT NULL,
                    PRIMARY KEY (matricula)
                  );'''

        sql2 = '''CREATE TABLE IF NOT EXISTS tbnota (
                    item INTEGER PRIMARY KEY AUTOINCREMENT,
                    valor FLOAT NOT NULL,
                    matricula INTEGER NOT NULL,
                    FOREIGN KEY (matricula) REFERENCES tbaluno(matricula)
                  );'''

        cursor.execute(sql1)
        cursor.execute(sql2)
        conexao.commit()

        print('Banco de dados criado e tabelas prontas.')

    except conector.DatabaseError as err:
        print('Erro de banco de dados:', err)
    
    finally:
        if conexao:
            cursor.close()
            conexao.close()

# Função para adicionar aluno
def adicionar_aluno(matricula, nome, curso):
    try:
        conexao = conector.connect('registro_notas.db')
        cursor = conexao.cursor()

        sql = 'INSERT INTO tbaluno (matricula, nome, curso) VALUES (?, ?, ?)'
        cursor.execute(sql, (matricula, nome, curso))
        conexao.commit()

        print('Aluno inserido com sucesso!')

    except conector.DatabaseError as err:
        print('Erro ao inserir aluno:', err)

    finally:
        if conexao:
            cursor.close()
            conexao.close()

# Função para listar alunos
def listar_alunos():
    try:
        conexao = conector.connect('registro_notas.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM tbaluno')
        alunos = cursor.fetchall()

        if alunos:
            for aluno in alunos:
                print(f"Matricula: {aluno[0]}, Nome: {aluno[1]}, Curso: {aluno[2]}")
        else:
            print("Nenhum aluno encontrado.")

    except conector.DatabaseError as err:
        print('Erro ao listar alunos:', err)

    finally:
        if conexao:
            cursor.close()
            conexao.close()

# Função para atualizar dados de um aluno
def atualizar_aluno(matricula, nome=None, curso=None):
    try:
        conexao = conector.connect('registro_notas.db')
        cursor = conexao.cursor()

        if nome and curso:
            sql = 'UPDATE tbaluno SET nome = ?, curso = ? WHERE matricula = ?'
            cursor.execute(sql, (nome, curso, matricula))
        elif nome:
            sql = 'UPDATE tbaluno SET nome = ? WHERE matricula = ?'
            cursor.execute(sql, (nome, matricula))
        elif curso:
            sql = 'UPDATE tbaluno SET curso = ? WHERE matricula = ?'
            cursor.execute(sql, (curso, matricula))

        conexao.commit()
        print('Dados do aluno atualizados com sucesso!')

    except conector.DatabaseError as err:
        print('Erro ao atualizar aluno:', err)

    finally:
        if conexao:
            cursor.close()
            conexao.close()

# Função para deletar um aluno
def deletar_aluno(matricula):
    try:
        conexao = conector.connect('registro_notas.db')
        cursor = conexao.cursor()

        sql = 'DELETE FROM tbaluno WHERE matricula = ?'
        cursor.execute(sql, (matricula,))
        conexao.commit()

        print('Aluno deletado com sucesso!')

    except conector.DatabaseError as err:
        print('Erro ao deletar aluno:', err)

    finally:
        if conexao:
            cursor.close()
            conexao.close()

# Função para adicionar uma nota
def adicionar_nota(valor, matricula):
    try:
        conexao = conector.connect('registro_notas.db')
        cursor = conexao.cursor()

        sql = 'INSERT INTO tbnota (valor, matricula) VALUES (?, ?)'
        cursor.execute(sql, (valor, matricula))
        conexao.commit()

        print('Nota inserida com sucesso!')

    except conector.DatabaseError as err:
        print('Erro ao inserir nota:', err)

    finally:
        if conexao:
            cursor.close()
            conexao.close()

# Função para listar notas de um aluno
def listar_notas(matricula):
    try:
        conexao = conector.connect('registro_notas.db')
        cursor = conexao.cursor()

        cursor.execute('SELECT * FROM tbnota WHERE matricula = ?', (matricula,))
        notas = cursor.fetchall()

        if notas:
            print(f"Notas do aluno com matrícula {matricula}:")
            for nota in notas:
                print(f"Item: {nota[0]}, Nota: {nota[1]}")
        else:
            print("Nenhuma nota encontrada para esse aluno.")

    except conector.DatabaseError as err:
        print('Erro ao listar notas:', err)

    finally:
        if conexao:
            cursor.close()
            conexao.close()

# Programa principal para testar as funções CRUD
if __name__ == '__main__':
    criar_tabelas()  # Criar as tabelas se não existirem

    # Inserir alunos
    adicionar_aluno(123, 'João Silva', 'Engenharia')
    adicionar_aluno(456, 'Maria Souza', 'Matemática')

    # Listar alunos
    listar_alunos()

    # Atualizar dados de um aluno
    atualizar_aluno(123, nome='João Pedro', curso='Engenharia Civil')

    # Listar alunos após atualização
    listar_alunos()

    # Adicionar notas
    adicionar_nota(9.5, 123)
    adicionar_nota(8.0, 123)
    adicionar_nota(7.5, 456)

    # Listar notas de um aluno
    listar_notas(123)

    # Deletar um aluno
    deletar_aluno(456)

    # Listar alunos após deleção
    listar_alunos()

    print('Fim do programa.')