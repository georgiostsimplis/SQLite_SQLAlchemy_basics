import sqlite3

# The 1st time that we run this function creates a database
# The 2nd time that we run this function conects us to the database
connection = sqlite3.connect('movies.db')

# To create a table in our database we need to grab the cursor object
cursor = connection.cursor()

famousFilms = [('Pulp Fiction', 'Quentin Tarantino', 1994),
               ('Back to the Future', 'Robert Zemeckis', 1985),
               ('Moonrise Kingdom', 'Wes Anderson', 2012)]

# Insert Multiple records from the above list
cursor.executemany(' INSERT INTO Movies VALUES (?,?,?)', famousFilms)

# Retrieve Table from the database
cursor.execute(''' SELECT * FROM Movies''')

# Retrieve a single row
print(cursor.fetchall())


# To save changes
connection.commit()

# To close the connection
connection.close()