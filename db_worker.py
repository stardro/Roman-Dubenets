print("db_worker")
import sqlite3

db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users(
    idworker INT PRIMARY KEY,
    first name TEXT,
    family name TEXT,
    age DATE
);""")

db.commit()
sql.execute("""CREATE TABLE IF NOT EXISTS salery(
    idworker INT PRIMARY KEY,
    mount salery INT,
    totalsum BIGINT
);""")
db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS position(
    idworker INT PRIMARY KEY,
    position TEXT,
    experience TEXT
);""")
db.commit()

user_idworker = input("ID Працівника: ")
user_first name=input("")


sql.execute("SELECT idworker FROM users")
if sql.fetchone() is None:
    sql.execute("INSERT INTO users VALUE(?,?,?,?}",(user_idworker, ))
    db.commit()

    print("Записано!")
else:
    print("Такий id вже записаний!")

    for value in sql.execute("SELECT * FROM users"):
        print(value[])
    
    
