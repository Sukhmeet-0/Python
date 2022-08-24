import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="1494",database="telusko")

mycursor=mydb.cursor()
mycursor.execute("select * from student")
result=mycursor.fetchone()
for i in mycursor:
	print(i)

