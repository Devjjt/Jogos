import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Alves@01',
    database='projeto',
)
cursor = conexao.cursor()

# CRUD

# CREATE
nome_produto = "Yamaha Fazer FZ25"
valor = 30000
nome_cliente = "Ruan"
comando = f'INSERT INTO vendas (nome_produto, valor, nome_cliente) VALUES ("{nome_produto}", {valor}, "{nome_cliente}")'
cursor.execute(comando)
conexao.commit() # edita o banco de dados

# READ
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() # ler o banco de dados
print(resultado)

# UPDATE
nome_produto = "Honda Biz"
valor = 10000
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

# Delete
nome_cliente = "Gael"
comando = f' DELETE FROM vendas WHERE nome_cliente = "{nome_cliente}"'
cursor.execute(comando)
conexao.commit()



cursor.close()
conexao.close()