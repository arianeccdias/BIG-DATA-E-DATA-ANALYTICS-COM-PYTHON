import sqlite3

#inicializa a conexao com o banco de dados
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as querys (comandos)
c = conn.cursor ()

#executa o comanod em SQL
c.execute("""ALTER TABLE usuarios ADD data_nascimento VARCHAR(10)""")

print("Adicionado nova coluna 'data_nascimento' dentro da tabela 'usuarios' com sucesso!")

#grava informações no banco de dados
conn.commit()

#encerrar a conexão com o banco de dados
conn.close()
