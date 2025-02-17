# sql lite connection

import sqlite3
conn = sqlite3.connect("my_database.db")

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
)
""")

# Insert data
def insert_user(name,age):
    cursor.execute("INSERT INTO users (name, age) VALUES(?,?)",(name,age))
    conn.commit()
insert_user("aman",21)



def update_user(user_id,new_age):
    cursor.execute("UPDATE users SET age=? WHERE id=?",(new_age,user_id))
    conn.commit()

update_user(1,24)


def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id=?",(user_id,))
    conn.commit()
    print("User deleted sucessfully :")

delete_user(11)


def get_user():
    cursor.execute("SELECT* FROM users")
    users=cursor.fetchall()
    for user in users:
        print(user)

get_user()

conn.close()


# # using Mysql-connector

import mysql.connector
connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="King#123",
    database="testDb"
)
if connection.is_connected():
    print("connection successful :")
# create cursor object
cursor=connection.cursor()
# drop table (delete table )
dr="drop table users"
cursor.execute(dr)
connection.commit()
# # SQL query to create the table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(255) UNIQUE
)
"""

# Execute the query
cursor.execute(create_table_query)

# Commit the transaction
connection.commit()

print("Table created ")

# ## insert data into table 
insert_query = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)"

# # List of records (tuples)
records = [
    ("Alice", 28, "alice@example.com"),
    ("Bob", 32, "bob@example.com"),
    ("Charlie", 25, "charlie@example.com"),
    ("David", 30, "david@example.com"),
    ("Eve", 27, "eve@example.com")
]

# Execute multiple inserts
cursor.executemany(insert_query, records) # executemany() for multiple record insertion 
connection.commit()
print("record added :")


# # read from the record
read="select* from users"
cursor.execute(read)
rows=cursor.fetchall()

for row in rows:
    print(row)



# # alter table 
alter="ALTER table users  add column phone varchar(20)"
cursor.execute(alter)
print("column added ")

# # rename using alter (Phone----> Mobile)
rename = "ALTER TABLE users CHANGE COLUMN phone mobile VARCHAR(20)"
cursor.execute(rename)
print("remaned successfully ")


# # update 
update="UPDATE users SET age=%s WHERE name=%s"
data=(25,"")
cursor.execute(update)


# # delete 
delete="delete from users where name=%s"
data=("ABC",)
cursor.execute(delete,data)
print("record deleted ")
connection.commit()

# truncate table (remove all data from table)
trun="truncate table users"
cursor.execute(trun)
print("Truncate successful :")
connection.commit()





#limit() clause (retrieve geven number of record from table)
lim="select * from users limit %s"
data=(3,)
cursor.execute(lim,data)
result=cursor.fetchall()
for row in result:
    print(row)


# delete specific column
alt="alter table users drop column mobile;"
cursor.execute(alt)
connection.commit()
print("successful")

# Order by (sort the record )
fil="select*from users ORDER BY age ASC"
cursor.execute(fil)
result=cursor.fetchall()
for row in result:
    print(row)




# create table

cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    salary INT
)
""")
# Create Employees Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INT
)
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    dept_id INT AUTO_INCREMENT PRIMARY KEY,
    dept_name VARCHAR(100)
)
""")

# Insert Sample Data into Employees Table
cursor.executemany("INSERT INTO employees (emp_name, dept_id) VALUES (%s, %s)", [
    ("Alice", 1),
    ("Bob", 2),
    ("Charlie", 3),
    ("David", None),  
    ("Eve", 1)
])

# Insert Sample Data into Departments Table
cursor.executemany("INSERT INTO departments (dept_id, dept_name) VALUES (%s, %s)", [
    (1, "HR"),
    (2, "IT"),
    (3, "Finance"),
    (4, "Marketing")  
])


cursor.executemany("INSERT INTO employee (name, salary) VALUES (%s, %s)", [
    ('Alice', 50000),
    ('Bob', 60000),
    ('Charlie', 70000),
    ('David', 80000),
    ('Eve', 90000)
])
# cursor.execute("INSERT INTO employees (name, salary) VALUES ('Alice', 50000)")
# cursor.execute("INSERT INTO employees (name, salary) VALUES ('Bob', 60000)")
# cursor.execute("INSERT INTO employees (name, salary) VALUES ('Charlie', 70000)")
# cursor.execute("INSERT INTO employees (name, salary) VALUES ('David', 80000)")
# cursor.execute("INSERT INTO employees (name, salary) VALUES ('Eve', 90000)")
# connection.commit()
# print("table created ")

# aggregation function ( Sum,min,max,average,count)

cursor.execute("select SUM(salary) from employees")
total_salary=cursor.fetchone()[0]
print(total_salary)

# average
cursor.execute("select AVG(salary) from employees")
average_salary=cursor.fetchone()[0]
print(f"Average salary is: {average_salary}")

# Min
cursor.execute("select max(salary) from employees")
max_salary=cursor.fetchone()[0]
print(f"Max salary is : {max_salary}")

# min salary
cursor.execute("select MIN(salary) from employees")
min_salary=cursor.fetchone()[0]
print(f"Min salary is :{min_salary}")

# count 
cursor.execute("select COUNT(*) from employees")
count_emp=cursor.fetchone()[0]
print(f"taotal employees are :{count_emp}")


# Inner Join 
query="""select employees.emp_name, departments.dept_name 
from employees
inner join departments on employees.dept_id=departments.dept_id """
cursor.execute(query)
print("INNER JOIN ---->")
for rows in cursor.fetchall():
    print(rows)


# Right join
query=""" select employees.emp_name,departments.dept_name
from employees
right join departments on employees.dept_id=departments.dept_id;
"""
cursor.execute(query)
print("Right Join ")
for row in cursor.fetchall():
    print(row)

# left Join 
query=""" select employees.emp_name, departments.dept_name
from employees
left join departments on employees.dept_id=departments.dept_id;
"""
cursor.execute(query)
print("Left join ")
for raw in cursor.fetchall():
    print(raw)


# Close the cursor and connection    
cursor.close()
connection.close()