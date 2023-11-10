import sqlite3

banco_de_dados = "cliente.db"

conectar = sqlite3.connect(banco_de_dados)
seta = conectar.cursor()
seta.execute("CREATE TABLE IF NOT EXIST cliente (if INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
conectar.commit()
conectar.close()

