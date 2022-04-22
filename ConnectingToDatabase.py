import mysql.connector # the library we'll use to connect to the database

db = mysql.connector.connect( # the instruction to connect
    host="localhost",  # host name
    user="root", # user level or type
    password="whatever your password is", # password of database
    database="which database" # database you want to connect to
)
cursor = db.cursor() # the tool for data transfer
