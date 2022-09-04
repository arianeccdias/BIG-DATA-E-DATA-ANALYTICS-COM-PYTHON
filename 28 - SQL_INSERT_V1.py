import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db_py.db")

# Iniciliza o cursor onde sera feita as Querys 
c = conn.cursor()

# Define a Query e executa
c.execute("""INSERT INTO usuarios(nome, email, senha, data_nascimento) VALUES ('Joao','joao_e_maria@gmail.com','Maria123','21/05/2001')""")
c.execute("""INSERT INTO usuarios(nome, email, senha, data_nascimento) VALUES ('Maria','maria_e_joao@gmail.com','Joao123','21/05/2001')""")
c.execute("""INSERT INTO usuarios(nome, email, senha, data_nascimento) VALUES ('Ana','aninha@gmail.com','Joao123','21/05/2001)""")

# Mostra mensagem para o usuario
print("Usuarios Adicionados com sucesso V1")

# Grava no banco 
conn.commit()

# Fechar a conexão com banco de dados
conn.close()