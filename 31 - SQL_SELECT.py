import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db_py.db")

# Iniciliza o cursor onde sera feita as Querys 
c = conn.cursor()

# Define a Query e executa
c.execute("""SELECT * FROM usuarios""")

# Mostra mensagem para o usuario
for linha in c.fetchall():
    print(linha)

# Fechar a conexão com banco de dados
conn.close()