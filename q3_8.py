import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Hosppdd",
        port='3307',
    )

    cursor = mydb.cursor()

    # Creating the Opinion table. opinion is a child of rating, hence the id of opinion is a foreign key to the Rating
    # table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Opinion (
            ID INT PRIMARY KEY,
            comment TEXT NOT NULL,
            
            FOREIGN KEY (ID) REFERENCES Rating (ID)
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()