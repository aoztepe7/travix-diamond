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


def update(Shop):
    db_connection = None
    try:
        db_connection = mysql.connector.connect(host=getHost(),user=getUser(),password= getPassword(),database=getDatabase())
        cursor = db_connection.cursor()
        query = """UPDATE shop set name=%s,commercial=%s,area_id=%s,phone=%s,mail=%s,landing=%s,vip_rep=%s,vip_comp=%s,currency=%s,rep_payment,version=%s WHERE id=%s and version=%s and status=%s"""
        oldVersion = Shop.version
        Shop.version = int(Shop.version) + 1
        query_tuple= (Shop.name,Shop.commercial,Shop.areaId,Shop.phone,Shop.mail,Shop.landing,Shop.vipRep,Shop.vipComp,Shop.currency,Shop.currency,Shop.repPayment,(Shop.version),int(Shop.id),int(oldVersion),int(Shop.status))
        cursor.execute(query,query_tuple)
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        db_connection.close()

def create(Shop):
    db_connection = None
    try:
        db_connection = mysql.connector.connect(host=getHost(),user=getUser(),password= getPassword(),database=getDatabase())
        cursor = db_connection.cursor()
        query = """INSERT INTO shop (name,commercial,area_id,phone,mail,landing,vip_rep,vip_comp,currency,rep_payment,version,status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        query_tuple= (Shop.name,Shop.commercial,Shop.areaId,Shop.phone,Shop.mail,Shop.landing,Shop.vipRep,Shop.vipComp,Shop.currency,Shop.repPayment,Shop.version,int(Shop.status))
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
        query = """UPDATE shop set status = null where id = %s and version=%s"""
        query_tuple = (id,version)
        cursor.execute(query,query_tuple)
        db_connection.commit()
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        db_connection.commit()
