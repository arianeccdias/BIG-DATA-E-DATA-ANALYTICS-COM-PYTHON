import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db_py.db")

# Iniciliza o cursor onde sera feita as Querys 
c = conn.cursor()

# Define a Query e executa
c.execute("""ALTER TABLE usuarios ADD data_nascimento VARCHAR(10)""")

print("Tabela Usuarios Alterada com sucesso")

# Grava no banco 
conn.commit()

# Fechar a conexão com banco de dados
conn.close()