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

    # Creating the Doctor table.
    # A doctor's Identifier consists of his ID and his hospital ID.
    # Each doctor has a counselor, which is also a doctor.
    # Note: Using NOT NULL is important since every doctor has a counselor, but it will give us a hard time when trying
    # to create the first doctor
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Doctor (
            ID INT,
            hospital INT,
            name TEXT NOT NULL,
            counselor_id INT NOT NULL,
            counselor_hospital INT NOT NULL,
            
            PRIMARY KEY (ID, hospital),
            FOREIGN KEY (counselor_id, counselor_hospital) REFERENCES Doctor (ID, hospital),
            FOREIGN KEY (hospital) REFERENCES Hospital (ID)
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()