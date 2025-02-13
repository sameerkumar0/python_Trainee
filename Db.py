# # sql lite connection

# import sqlite3
# conn = sqlite3.connect("my_database.db")

# # Create a cursor object to execute SQL commands
# cursor = conn.cursor()

# # Create a table
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER
# )
# """)

# # # Insert data
# # def insert_user(name,age):
# #     cursor.execute("INSERT INTO users (name, age) VALUES(?,?)",(name,age))
# #     conn.commit()
# # insert_user("aman",21)



# # def update_user(user_id,new_age):
# #     cursor.execute("UPDATE users SET age=? WHERE id=?",(new_age,user_id))
# #     conn.commit()

# # update_user(1,24)


# # def delete_user(user_id):
# #     cursor.execute("DELETE FROM users WHERE id=?",(user_id,))
# #     conn.commit()
# #     print("User deleted sucessfully :")

# # delete_user(11)


# # def get_user():
# #     cursor.execute("SELECT* FROM users")
# #     users=cursor.fetchall()
# #     for user in users:
# #         print(user)

# # get_user()

# # conn.close()


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
## drop table (delete table )
# dr="drop table users"
# cursor.execute(dr)
# connection.commit()
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

# print("Table created ")

# ## insert data into table 
# insert_query = "INSERT INTO users (name, age, email) VALUES (%s, %s, %s)"

# # List of records (tuples)
# records = [
#     ("Alice", 28, "alice@example.com"),
#     ("Bob", 32, "bob@example.com"),
#     ("Charlie", 25, "charlie@example.com"),
#     ("David", 30, "david@example.com"),
#     ("Eve", 27, "eve@example.com")
# ]

# Execute multiple inserts
# cursor.executemany(insert_query, records) # executemany() for multiple record insertion 
# connection.commit()
# print("record added :")


# # read from the record
# read="select* from users"
# cursor.execute(read)
# rows=cursor.fetchall()

# for row in rows:
#     print(row)



# # alter table 
# alter="ALTER table users  add column phone varchar(20)"
# cursor.execute(alter)
# print("column added ")

# # rename using alter (Phone----> Mobile)
# rename = "ALTER TABLE users CHANGE COLUMN phone mobile VARCHAR(20)"
# cursor.execute(rename)
# print("remaned successfully ")


# # update 
# update="UPDATE users SET age=%s WHERE name=%s"
# data=(25,"")
# cursor.execute(update)


# # delete 
# delete="delete from users where name=%s"
# data=("ABC",)
# cursor.execute(delete,data)
# print("record deleted ")
# connection.commit()

# truncate table (remove all data from table)
# trun="truncate table users"
# cursor.execute(trun)
# print("Truncate successful :")
# connection.commit()

# Close the cursor and connection



#limit() clause (retrieve geven number of record from table)
# lim="select * from users limit %s"
# data=(3,)
# cursor.execute(lim,data)
# result=cursor.fetchall()
# for row in result:
#     print(row)

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

cursor.close()
connection.close()