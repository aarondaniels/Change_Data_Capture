#pip install pymysql
#pip install cryptography
# import pymysql

import mysql.connector
from datetime import datetime
import atexit
import uuid

cnx = mysql.connector.connect(user='root', 
    password='MyNewPass',
    host='127.0.0.1',
    db='pluto')

# create cursor
cursor = cnx.cursor()

# write stamp to posts table
def write(): 
    # insert
    id = str(uuid.uuid4())
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = (f'INSERT INTO `posts` VALUES("{id}","{time}")')
    cursor.execute(query)
    cnx.commit()

# read posts table
def read():
    # get last 5 entries
    query = ("SELECT * FROM posts ORDER BY stamp DESC LIMIT 5;")
    cursor.execute(query)

    # read rows
    stamps = []
    for row in cursor.fetchall():
        # print(row)
        stamps.append(row[1])
    return stamps

# delete posts table data
def delete():
    # get last 5 entries
    query = ("TRUNCATE posts")
    cursor.execute(query)
    cnx.commit()    


@atexit.register
def exit_handler():
    cursor.close()
    cnx.close()   