import mysql.connector
from db.connection import *
GL_USER_ROLE = None

def logIn(username,password):
    db_connection = None
    global GL_USER_ROLE
    try:
        db_connection = mysql.connector.connect(host=getHost(),user=getUser(),password= getPassword(),database=getDatabase())
        cursor = db_connection.cursor()
        query = """SELECT * FROM USER WHERE username =%s and password =%s and status = true"""
        query_tuple =(username,password)
        cursor.execute(query,query_tuple)
        result = cursor.fetchall()
        if(result):
            GL_USER_ROLE= result[0][4]
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
    finally:
        db_connection.close()
