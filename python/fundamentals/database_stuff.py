import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="users_db"
)

if db.is_connected():
    print("connected")
else:
    print("no")

mc = db.cursor()

sql = "INSERT INTO users_tbl (first_name, last_name, email) VALUES (%s, %s, %s)"
val = ("Guy", "There", "email@dot.com")
mc.execute(sql, val)
db.commit()