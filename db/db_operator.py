import mysql.connector
from db.connection import *

def list(query):
    db_connection = None
    try:
        db_connection = mysql.connector.connect(host=getHost(),user=getUser(),password= getPassword(),database=getDatabase())
        cursor = db_connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        if(result):
            return result
        else:
            return None
    except Exception as e:
        print(e)
        return None
    finally:
        db_connection.close()


def update(Operator):
    db_connection = None
    try:
        db_connection = mysql.connector.connect(host=getHost(),user=getUser(),password= getPassword(),database=getDatabase())
        cursor = db_connection.cursor()
        query = """UPDATE operator set name=%s,chief_com=%s,version=%s WHERE id=%s and version=%s and status=%s"""
        oldVersion = Operator.version
        Operator.version = int(Operator.version) + 1
        query_tuple= (Operator.name,float(Operator.chief_com),int(Operator.version),int(Operator.id),int(oldVersion),int(Operator.status))
        cursor.execute(query,query_tuple)
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        db_connection.close()

def create(Operator):
    db_connection = None
    try:
        db_connection = mysql.connector.connect(host=getHost(),user=getUser(),password= getPassword(),database=getDatabase())
        cursor = db_connection.cursor()
        query = """INSERT INTO operator (name,chief_com,version,status) VALUES (%s,%s,%s,%s)"""
        query_tuple= (Operator.name,float(Operator.chief_com),Operator.version,int(Operator.status))
        cursor.execute(query,query_tuple)
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        db_connection.close()

def delete(id,version):
    db_connection = None
    try:
        db_connection = mysql.connector.connect(host=getHost(), user=getUser(), password=getPassword(),
                                                database=getDatabase())
        cursor = db_connection.cursor()
        query = """UPDATE operator set status = null where id = %s and version=%s"""
        query_tuple = (id,version)
        cursor.execute(query,query_tuple)
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        db_connection.commit()
