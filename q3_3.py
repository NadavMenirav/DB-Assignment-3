import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Hosppdd", # Creating the table in the Hosppdd DB
        port='3307',
    )

    cursor = mydb.cursor()

    # Creating the Hospital table. It does not depend on any other table. ID is the primary key, and the name shall not
    # be null.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Hospital (
            ID INT PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()