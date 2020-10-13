import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="luminar_python_sql"
)#open database connection

cursor=db.cursor()

#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#execute sql query using execute() method

#sql='CREATE TABLE EMPLOYEE (FIRST_NAME CHAR(20),LAST_NAME CHAR(25),AGE INT,SEX CHAR(1),INCOME INT)'
#cursor.execute(sql)

#query="""INSERT INTO EMPLOYEE(FIRST_NAME,   LAST_NAME,AGE,SEX,INCOME) VALUES("AKSHAY","DHANYA",22,"F",2000)   """

#sql="SELECT FIRST_NAME FROM EMPLOYEE WHERE INCOME > 5000 "


try:
    cursor.execute("SELECT FIRST_NAME FROM EMPLOYEE WHERE INCOME >= 5000 ")

    #db.commit()
    relt=cursor.fetchall()

    for re in relt:
        print(re)

except Exception as e:
    db.rollback()#partial changes are undone
    print(e.args)

finally:
    db.close()