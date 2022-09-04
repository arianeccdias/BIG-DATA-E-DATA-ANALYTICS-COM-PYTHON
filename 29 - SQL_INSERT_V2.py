import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db_py.db")

# Iniciliza o cursor onde sera feita as Querys 
c = conn.cursor()

# Cria a lista de usuarios
lista = [
    ('Joao','joao_e_maria@gmail.com','Maria123','21/05/2001'),
    ('Maria','maria_e_joao@gmail.com','Joao123','21/05/2001'),
    ('Ana','aninha@gmail.com','Joao123','21/05/2001')
]

# Define a Query e executa
c.executemany("""INSERT INTO usuarios(nome, email, senha, data_nascimento) VALUES (?,?,?,?)""",lista)

# Mostra mensagem para o usuario
print("Usuarios Adicionados com sucesso V2")

# Grava no banco 
conn.commit()

# Fechar a conexão com banco de dados
conn.close()