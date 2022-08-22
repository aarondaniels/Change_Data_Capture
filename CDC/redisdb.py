#pip install redis
import redis

from mongodb import delete

client = redis.Redis(host='localhost', port=6379, db=0)

def write(stamps):
    client.mset({"LastInsertDate": f"{str(stamps[0])}" })

def read():
    return client.get("LastInsertDate")

def delete():
    client.delete('LastInsertDate')