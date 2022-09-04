import sqlite3

#inicializa a conexao com o banco de dados
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as querys (comandos)
c = conn.cursor ()

#executa o comanod em SQL
c.execute("""INSERT INTO usuarios(nome, email, senha, data_nascimento)
VALUES('Joao', 'joao_e_maria@gmail.com', 'Maria123', '21/05/2001')""")

c.execute("""INSERT INTO usuarios(nome, email,senha, data_nascimento)
VALUES('Maria', 'maria_e_joao@gmail.com', 'Joao123', '21/05/2001')""")

c.execute("""INSERT INTO usuarios(nome, email, senha, data_nascimento)
VALUES('Ana', 'aninha@gmail.com', 'Joao123', '21/05/2001')""")

print("Adicionado novos usuarios na tabela 'usuario' ")

#grava informações no banco de dados
conn.commit()

#encerrar a conexão com o banco de dados
conn.close()
