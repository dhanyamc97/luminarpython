import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
)#open database connection

cursor=db.cursor()

#execute sql query using execute() method
sql="SELECT VERSION()"
cursor.execute(sql)

#fetch a single row using fetchon() method
data=cursor.fetchone()
print("Database Version:",data)

db.close()




