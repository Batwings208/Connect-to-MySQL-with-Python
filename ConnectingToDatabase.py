import mysql.connector # the library we'll use to connect to the database

db = mysql.connector.connect( # the instruction to connect
    host="localhost",  # host name
    user="root", # use level or type
    password="root54321", # password of database
    database="Car" # database you want to connect to
)
cursor = db.cursor() # the tool for data transfer
