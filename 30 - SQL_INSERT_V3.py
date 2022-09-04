import sqlite3

# Inicializa a conexão com o banco de dados
conn = sqlite3.connect("db_py.db")

# Iniciliza o cursor onde sera feita as Querys 
c = conn.cursor()

# Carrega as informações do usuario
p_nome = input('Nome: ')
p_email = input('Email: ')
p_senha = input('Senha: ')
p_data_de_nascimento = input('Data de Nascimento (dd/mm/yyyy): ')


# Define a Query e executa
c.execute("""INSERT INTO usuarios(nome, email, senha, data_nascimento) VALUES (?,?,?,?)""",(p_nome, p_email, p_senha, p_data_de_nascimento))

# Mostra mensagem para o usuario
print("Usuarios Adicionados com sucesso V3")

# Grava no banco 
conn.commit()

# Fechar a conexão com banco de dados
conn.close()