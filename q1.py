import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mysql", # Using the mysql Database when creating a new DB
        port='3307',
    )

    cursor = mydb.cursor()

    # Named the DB Hosppdd. Used 'IF NOT EXISTS' To prevent errors when running twice.
    cursor.execute("""
        CREATE DATABASE IF NOT EXISTS Hosppdd;
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()