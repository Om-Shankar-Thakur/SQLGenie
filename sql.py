# Import module
import sqlite3

# Connecting to sqlite
conn = sqlite3.connect('student.db')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()

# Creating table only if it does not exist
table = """CREATE TABLE IF NOT EXISTS STUDENT1(
            NAME VARCHAR(255), 
            CLASS VARCHAR(255), 
            SECTION VARCHAR(255), 
            MARKS INT);"""
cursor.execute(table)

# Delete existing records from the table
cursor.execute('DELETE FROM STUDENT1')

# Queries to INSERT records.
cursor.execute('''INSERT INTO STUDENT1 VALUES ('Om', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT1 VALUES ('Raj', 'Data Science', 'B', 81)''')
cursor.execute('''INSERT INTO STUDENT1 VALUES ('Piyush', 'Devops', 'C', 78)''')
cursor.execute('''INSERT INTO STUDENT1 VALUES ('Umang', 'Data Science', 'C', 35)''')
cursor.execute('''INSERT INTO STUDENT1 VALUES ('Aniket', 'Devops', 'A', 89)''')
cursor.execute('''INSERT INTO STUDENT1 VALUES ('Shubham', 'Data Science', 'B', 57)''')
cursor.execute('''INSERT INTO STUDENT1 VALUES ('Dinesh', 'Data Science', 'C', 38)''')
cursor.execute('''INSERT INTO STUDENT1 VALUES ('Ram', 'Devops', 'A', 84)''')

# Display data inserted
print("Data Inserted in the table: ")
data = cursor.execute('''SELECT * FROM STUDENT1''')
for row in data:
    print(row)

# Commit your changes in the database
conn.commit()

# Closing the connection
conn.close()
