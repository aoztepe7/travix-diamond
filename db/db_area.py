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


def update(Area):
    db_connection = None
    try:
        db_connection = mysql.connector.connect(host=getHost(),user=getUser(),password= getPassword(),database=getDatabase())
        cursor = db_connection.cursor()
        query = """UPDATE area set name=%s,version=%s WHERE id=%s and version=%s and status=%s"""
        oldVersion = Area.version
        Area.version = int(Area.version) + 1
        query_tuple= (Area.name,int(Area.version),int(Area.id),int(oldVersion),int(Area.status))
        cursor.execute(query,query_tuple)
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        db_connection.close()

def create(Area):
    db_connection = None
    try:
        db_connection = mysql.connector.connect(host=getHost(),user=getUser(),password= getPassword(),database=getDatabase())
        cursor = db_connection.cursor()
        query = """INSERT INTO area (name,version,status) VALUES (%s,%s,%s)"""
        query_tuple= (Area.name,Area.version,int(Area.status))
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
        query = """UPDATE area set status = null where id = %s and version=%s"""
        query_tuple = (id,version)
        cursor.execute(query,query_tuple)
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        db_connection.commit()
