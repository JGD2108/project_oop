import sqlite3
con = sqlite3.connect("Domiciliario.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS Pedidos")
sql= """CREATE TABLE IF NOT EXISTS Pedidos(
        Name TEXT,
        Pedido TEXT,
        Total FLOAT,
        Ubicacion TEXT,
        Cel TEXT, 
        Estado TEXT
        )"""


"""
data = [
        ("Jose David",1001915145, 3043774896, "Available"),
        ("Cristian", 1001915145, 310554675, "Available"),
         ]

cur.executemany("INSERT INTO Domiciliarios VALUES(?, ?, ?,?)", data)
"""
cur.execute(sql)
con.commit()
con.close()