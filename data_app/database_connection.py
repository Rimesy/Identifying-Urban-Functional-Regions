import psycopg2

class connection():

    def __init__(self, inst_name):
        self.inst_name = inst_name
        self.connection = psycopg2.connect("dbname=postgres user=postgres password=reading11o4") # Connection to postgres database
        self.cursor = self.connection.cursor() # Create a cursor to perform operations in the database
        print("Connection opened: " + self.inst_name)

    # Method command sends an executable statement to the database
    def command(self, query):
        self.cursor.execute(query)
        print(self.inst_name + ": query executed successfully")

    # DO NOT USE (fetching all the data in the database is a probably a bad idea and never really necessary is it?)
    # Method fetchall returns all the data in the database 
    def fetchall(self):
        records = self.cursor.fetchall()
        return records
    
    # Method fetchone returns a python object of data queried in the database
    def fetchone(self):
        data_object = self.cursor.fetchone()
        return data_object
    
    # Method commit makes the changes to the database persistent
    def commit(self):
        self.connection.commit()

    # Method close quits the communication with the database
    def close(self):
        self.cursor.close()
        self.connection.close()
        print("Connection closed: " + self.inst_name)


