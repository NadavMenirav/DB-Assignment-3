import mysql.connector

if __name__ == '__main__':
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="## PUT THE CORRECT DATABASE HERE IF NEEDED ##",
        port='3307',
    )

    cursor = mydb.cursor()
    cursor.execute("""
    ## PUT YOUR QUERY ##
    """)

    # !!!Commit the transaction to save the changes to the database!!!
    mydb.commit()
    cursor.close()
    mydb.close()