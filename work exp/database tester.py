from __future__ import print_function

import mysql as my
import mysql.connector

mydb = mysql.connector.connect(
  host="34.251.24.146",
  user="ryan",
  passwd="Ry4nry4n!?",
  database="ryan"

)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM comments ORDER BY name limit 1000")

myresults = mycursor.fetchall()

for x in myresults:
  print(x)