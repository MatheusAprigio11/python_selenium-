import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    database='mega_sena',
    user='root',
    password=''
)


cursor = con.cursor()
