import os
import sys
import mysql.connector

# -------------
# input arguments
# -------------
# -create, create containers
# -init, init mysql and cassandra, others do not need it. 

# create container
def create(cmd, db):
    result = os.system(cmd)
    if (result == 0):
        print(f'Created {db}')

#initilize mysql db
def init_mysql():
    cnx = mysql.connector.connect(user = 'root',
        password = 'MyNewPass', 
        host = '127.0.0.1',
        database = '',
        auth_plugin='mysql_native_password')
    
    #create cursor
    cursor = cnx.cursor()

    #delete previous db
    query = ("DROP DATABASE IF EXISTS 'pluto';")
    cursor.exeucte(query)

    #create db
    query = ("CREATE DATABASE IF NOT EXISTS pluto")
    cursor.execute(query)

    #create table
    query = ('''
    CREATE TABLE posts(
        id VARCHAR(36),
        stamp VARCHAR(20)
    )
    ''')
    cursor.execute(query)

    #clean up
    cnx.commit()
    cursor.close()
    cnx.close()


# read input argument
argument = len(sys.argv)
if (argument > 1):
    argument = sys.argv[1]

# if -create input argument, create containers
if(argument == '-create'):
    create('docker run -p 3306:3306 --name some-mysql -e MYSQL_ROOT_PASSWORD=MyNewPass -d mysql', 'mysql')
    #this command can be repeated for other database types:
    #create('docker run -p 27017:27017 --name some-mongo -d mongo')
    #create('docker run -p 6379:6379 --name some-redis -d redis')
    #create('docker run -p 9042:9042 --name some-cassandra -d cassandra')
    sys.exit()

# if -init, init database
if(argument == '-init'):
    init_mysql()
    #init_cassandra()
    sys.exit()
