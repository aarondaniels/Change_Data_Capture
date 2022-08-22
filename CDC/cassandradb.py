#pip install cassandra-driver
from cassandra.cluster import Cluster
from cassandra.connection import EndPoint
from cassandra.query import END_BADCHAR_REGEX

keyspace = 'stamps'
cluster = Cluster(['localhost'], port=9042)
session = cluster.connect(keyspace)

def write(stamps):
    sql = f"update posts set stamp = '{str(stamps[0])}' where id = 'maxTimeStamp' IF EXISTS"
    session.execute(sql)


def read():
    result = session.execute("select stamp from posts where id = 'maxTimeStamp'")
    return result[0].stamp;

def delete():
    session.execute("delete from posts where id = 'maxTimeStamp'")