import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db_py.db")

# Iniciliza o cursor onde sera feita as Querys 
c = conn.cursor()

# Define a Query e executa
c.execute("""SELECT * FROM usuarios""")

# Mostra os dados da tabela para o usuario
for linha in c.fetchall():
    print(linha)

# Carrega as informações do usuario
id_usuario = input('Id do usuario: ')
novo_nome = input('Nome: ')
novo_email = input('Email: ')
nova_senha = input('Senha: ')
nova_data_de_nascimento = input('Data de Nascimento (dd/mm/yyyy): ')


# Define a Query e executa
c.execute("""UPDATE usuarios SET nome=?, email=?, senha=?, data_nascimento=? WHERE id=? """,(novo_nome, novo_email, nova_senha, nova_data_de_nascimento,id_usuario))

# Grava no banco 
conn.commit()

# Mostra mensagem para o usuario
print(f"Usuarios {id_usuario} modificado com sucesso V2")

# Fechar a conexão com banco de dados
conn.close()