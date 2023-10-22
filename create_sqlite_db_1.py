import sqlite3

# The 1st time that we run this function creates a database
# The 2nd time that we run this function conects us to the database
connection = sqlite3.connect('movies.db')

# To create a table in our database we need to grab the cursor object
cursor = connection.cursor()

# Now with the cursor we can execute commands or queries
cursor.execute(''' CREATE TABLE IF NOT EXISTS Movies 
               (Title TEXT, Director TEXT, Year INT) ''')


# Insert data into the movies.db
#cursor.execute(''' INSERT INTO Movies  VALUES('Taxi Driver', 'Martin Scorsese', 1976)''')

# Retrieve Table from the database
cursor.execute(''' SELECT * FROM Movies''')

# Retrieve a single row
print(cursor.fetchone())


# To save changes
connection.commit()

# To close the connection
connection.close()