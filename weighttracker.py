import sqlite3
from datetime import date 

peso = int(input("Qual o peso de hoje? \n\n"))

dia = date.today().day

mes = date.today().month

ano = date.today().year

data_pesagem = str("{} - {} - {}".format(dia, mes, ano))

conn = sqlite3.connect("peso.db")
c = conn.cursor()
c.execute("""CREATE TABLE peso (
            first text,
            second real
    )""")
     
c.execute("INSERT INTO peso Values (?,?)",(data_pesagem,peso))

conn.commit()

conn.close()
