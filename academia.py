import sqlite3 as conector #apelido
   #função para criar a estrutura da tabela
def criar_tabela():
    conexao = conector.connect('academia.db')
    cursor = conexao.cursor()
    
    sql = 'insert into cadastro (codigo, nome, idade) values (?, ?, ?)' #inserir registros
    cursor.execute(sql, (1286, 'Rodrigo Silva', 44))
    cursor.execute(sql, (1376, 'Marcus Saraiva', 24))
    #efetivação do comando
    conexao.commit()
    #fechamento das conexões
    cursor.close()
    conexao.close()

#executar função
criar_tabela()
print('Abra a pasta do programa e veja se o arquivo está lá')
print('Fim do programa')
