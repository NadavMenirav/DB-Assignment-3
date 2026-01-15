import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Hosppdd", # Using the Hosppdd DB
        port='3307',
    )

    cursor = mydb.cursor()

    # Creating the Medicine table first since it does not depend on other tables. The name of the medicine is not NULL
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Medicine (
            ID INT PRIMARY KEY,
            name TEXT NOT NULL
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()