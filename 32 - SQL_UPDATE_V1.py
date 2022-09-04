import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db_py.db")

# Iniciliza o cursor onde sera feita as Querys 
c = conn.cursor()

# Carrega as informações do usuario
id_usuario = 1
novo_nome = "Luiza"
novo_email = "luiza@uol.com.br"
nova_senha = "souLinda123"
nova_data_de_nascimento = "02/02/2002"

# Define a Query e executa
c.execute("""UPDATE usuarios SET nome=?, email=?, senha=?, data_nascimento=? WHERE id=? """,(novo_nome, novo_email, nova_senha, nova_data_de_nascimento,id_usuario))

# Grava no banco 
conn.commit()

# Mostra mensagem para o usuario
print(f"Usuarios {id_usuario} modificado com sucesso V1")

# Fechar a conexão com banco de dados
conn.close()