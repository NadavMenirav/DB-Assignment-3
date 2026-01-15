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

    # Creating the Rating table.
    # Assuming the rating is an integer (for example 1-10 or 1-5).
    # Each rating has a unique patient who is the rater (one-to-one relation)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Rating (
            ID INT PRIMARY KEY,
            rating INT NOT NULL,
            patient INT UNIQUE NOT NULL,
            
            FOREIGN KEY (patient) REFERENCES Patient (ID)
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()