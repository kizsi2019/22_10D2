import mysql.connector

db = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        passwd="",
                        database="mozi",

                                    )
mycursor = db.cursor()
mycursor.execute("SELECT * FROM vetites")

for x in mycursor:
    print(x)