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

    # Creating the Disease table. It depends on Medicine table since each disease has one medicine
    # (hence the foreign key).
    # Assuming that severity is an integer (for example severity from 1 to 10)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Disease (
            ID INT PRIMARY KEY,
            name TEXT NOT NULL,
            severity INT NOT NULL,
            medicine INT NOT NULL,
            
            FOREIGN KEY (medicine) REFERENCES Medicine (ID)
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()