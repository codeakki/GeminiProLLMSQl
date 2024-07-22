import sqlite3



## Connect to Sqlite3 database

connection=sqlite3.connect("student.db")

# Create a cursor object to insert record or create table 


cursor=connection.cursor()


#create the table 


table__info="""
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
"""
print(table__info)



cursor.execute(table__info)

##Insert Some more Records into the table

cursor.execute("Insert Into STUDENT values('Rahul','Data Science','A')")
cursor.execute("Insert Into STUDENT values('Akshay','Science','D')")
cursor.execute("Insert Into STUDENT values('Pankaj','Gaming','B')")
cursor.execute("Insert Into STUDENT values('Darius','Devops','A')")
cursor.execute("Insert Into STUDENT values('Dipesh','Devops','A')")

##Display all the records from the table

print("The inserted records are :")

data=cursor.execute('''Select * from STUDENT''')


for row in data:
    print(row)


 ## COmmit your changes to the database

connection.commit()
connection.close()      