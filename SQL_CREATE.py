import sqlite3

#inicializa a conexao com o banco de dados
conn = sqlite3.connect("db.db")

#inicializa o cursor onde sera feita as querys (comandos)
c = conn.cursor ()

#executa o comanod em SQL
c.execute("""CREATE TABLE usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50),
    email VARCHAR(100),
    senha VARCHAR(50)
)
""")

print("Tabela de usuarios criada com sucesso!")

#grava informações no banco de dados
conn.commit()

#encerrar a conexão com o banco de dados
conn.close()

