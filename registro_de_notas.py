# Importando a biblioteca de SQLite
import sqlite3 as conector

# Função para criar as tabelas no banco de dados
def criar_tabelas():
    try:
        # Abertura da conexão com o banco de dados 'registro_notas.db'
        conexao = conector.connect('registro_notas.db')

        # Aquisição de um cursor para executar comandos SQL
        cursor = conexao.cursor()

        # Comando SQL para criação da tabela 'tbaluno'
        sql1 = '''CREATE TABLE IF NOT EXISTS tbaluno (
                    matricula INTEGER NOT NULL,
                    nome TEXT NOT NULL,
                    curso TEXT NOT NULL,
                    PRIMARY KEY (matricula)
                  );'''

        # Comando SQL para criação da tabela 'tbnota'
        sql2 = '''CREATE TABLE IF NOT EXISTS tbnota (
                    item INTEGER PRIMARY KEY AUTOINCREMENT,
                    valor FLOAT NOT NULL,
                    matricula INTEGER NOT NULL,
                    FOREIGN KEY (matricula) REFERENCES tbaluno(matricula)
                  );'''

        # Execução dos comandos SQL para criar as tabelas
        cursor.execute(sql1)
        cursor.execute(sql2)

        # Efetivação das mudanças no banco de dados
        conexao.commit()

        print('Banco de dados criado e tabelas prontas.')
    
    except conector.DatabaseError as err:
        print('Erro de banco de dados:', err)
    
    finally:
        # Fechamento da conexão com o banco de dados
        if conexao:
            cursor.close()
            conexao.close()

# Chamando a função para criar as tabelas
criar_tabelas()