import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db_py.db")

# Iniciliza o cursor onde sera feita as Querys 
c = conn.cursor()

# Define a Query e executa
c.execute("""CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(50),
    email VARCHAR(100),
    senha VARCHAR(50)
    )""")

print("Tabela Usuarios Criada com sucesso")

# Grava no banco 
conn.commit()

# Fechar a conexão com banco de dados
conn.close()