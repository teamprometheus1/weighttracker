import sqlite3

conn = sqlite3.connect("peso.db")
c = conn.cursor()
c.execute("""CREATE TABLE (
            first text
            second real
    )""")
conn.commit()
conn.close()


