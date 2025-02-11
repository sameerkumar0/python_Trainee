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
# def insert_user(name,age):
#     cursor.execute("INSERT INTO users (name, age) VALUES(?,?)",(name,age))
#     conn.commit()
# insert_user("aman",21)



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
