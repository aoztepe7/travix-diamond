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


def update(Guide):
    db_connection = None
    try:
        db_connection = mysql.connector.connect(host=getHost(),user=getUser(),password= getPassword(),database=getDatabase())
        cursor = db_connection.cursor()
        query = """UPDATE guide set fullname=%s,phone=%s,mail=%s,guide_type=%s,version=%s WHERE id=%s and version=%s and status=%s"""
        oldVersion = Guide.version
        Guide.version = int(Guide.version) + 1
        query_tuple= (Guide.fullName,Guide.phone,Guide.mail,Guide.guide_type,int(Guide.version),int(Guide.id),int(oldVersion),int(Guide.status))
        cursor.execute(query,query_tuple)
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        db_connection.close()

def create(Guide):
    db_connection = None
    try:
        db_connection = mysql.connector.connect(host=getHost(),user=getUser(),password= getPassword(),database=getDatabase())
        cursor = db_connection.cursor()
        query = """INSERT INTO guide (fullname,phone,mail,guide_type,version,status) VALUES (%s,%s,%s,%s,%s,%s)"""
        query_tuple= (Guide.fullName,Guide.phone,Guide.mail,Guide.guide_type,Guide.version,int(Guide.status))
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
        query = """UPDATE guide set status = null where id = %s and version=%s"""
        query_tuple = (id,version)
        cursor.execute(query,query_tuple)
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        db_connection.commit()
