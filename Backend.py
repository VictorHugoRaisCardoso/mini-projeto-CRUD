import sqlite3 as sql

class TransactionObjetct():
    database = "cliente.db"
    conn = None
    cursor = None
    connected = False

    def connect(self):
        TransactionObjetct.conn = sql.connect(TransactionObjetct.database)
        TransactionObjetct.cursor = TransactionObjetct.conn.cursor()
        TransactionObjetct.connected = True

    def disconnect(self):
        TransactionObjetct.conn.close()
        TransactionObjetct.connected = False

    def execute(self, sql, params = None):
        if TransactionObjetct.connected:
            if params == None:
                TransactionObjetct.cursor.execute(sql)
            else:
                TransactionObjetct.cursor.execute(sql, params)
            return True
        else:
            return False
        
    def fetchall(self):
        return TransactionObjetct.cursor.fetchall()
    
    def persist(self):
        if TransactionObjetct.connected:
            TransactionObjetct.conn.commit()
            return True
        else:
            return False
    
def initDB():
    trans = TransactionObjetct()
    trans.connect()
    trans.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, sobrenome TEXT, email TEXT, cpf TEXT)")
    trans.persist()
    trans.disconnect()

initDB()

def view():
    trans = TransactionObjetct()
    trans.connect()

    trans.execute("SELECT * FROM clientes")

    rows = trans.fetchall()
    trans.disconnect()
    return rows

def insert(nome, sobrenome, email, cpf):
    trans = TransactionObjetct()
    trans.connect()
    trans.execute("INSERT INTO clientes VALUES(NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
    trans.persist()
    trans.disconnect()

    
