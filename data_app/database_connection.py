import psycopg2

class connection():

    def __init__(self):
        # Connection to postgres database
        self.connection = psycopg2.connect("dbname=postgres user=postgres password=reading11o4")

        # Create a cursor to perform operations in the database
        self.cursor = self.connection.cursor()

    # DO NOT USE (fetching all the data in the database is a probably a bad idea and never really necessary is it?)
    # Method fetchall returns all the data in the database 
    def fetchall(self):
        records = self.cursor.fetchall()
        return records
    
    # Method commit makes the changes to the database persistent
    def commit(self):
        self.connection.commit()

    # Method close quits the communication with the database
    def close(self):
        self.cursor.close()
        self.connection.close()

