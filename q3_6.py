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

    # Creating the Patient table.
    # Each patient has a doctor who takes care of him, a new diagnosis, and he can also have a previous diagnosis
    # Representing gender as a BIT: 0 for male, 1 for female
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Patient (
            ID INT PRIMARY KEY,
            name TEXT NOT NULL,
            weight INT NOT NULL,
            height INT NOT NULL,
            gender BIT NOT NULL,
            previous_disease INT,
            new_disease INT NOT NULL,
            doctor INT NOT NULL,
            hospital INT NOT NULL,
            
            FOREIGN KEY (previous_disease) REFERENCES Disease (ID),
            FOREIGN KEY (new_disease) REFERENCES Disease (ID),
            FOREIGN KEY (doctor, hospital) REFERENCES Doctor (ID, hospital)
        );
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()