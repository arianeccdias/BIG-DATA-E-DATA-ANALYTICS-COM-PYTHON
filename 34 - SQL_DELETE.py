import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db_py.db")

# Iniciliza o cursor onde sera feita as Querys 
c = conn.cursor()

# Carrega as informações do usuario
id_usuario = "5"

# Define a Query e executa
c.execute("""DELETE FROM usuarios WHERE id= ? """,(id_usuario))

# Grava no banco 
conn.commit()

# Mostra mensagem para o usuario
print(f"Usuario {id_usuario} deletado com sucesso")

# Fechar a conexão com banco de dados
conn.close()