import sqlalchemy


# This function conects us to the database
engine = sqlalchemy.create_engine('sqlite:///movies.db', echo=True)


# Create connection using engine
with engine.connect() as conn:
	result = conn.execute(sqlalchemy.text("SELECT * FROM Movies"))
	for row in result:
		print(row)