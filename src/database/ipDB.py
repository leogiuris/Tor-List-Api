
import sqlite3 as sl
import json

def connect_to_db():
    conn = sl.connect('src/database/ips_tor.db', check_same_thread=False)
    return conn



def createTables():

    conn = connect_to_db() 
    
    with conn:

        conn.execute("""
            CREATE TABLE banned_ip (
                ip_address TEXT PRIMARY KEY
            )
        """)

    print("tabelas criadas")

    conn.close()



def DropALL():

    SetDB()
    conn = connect_to_db() 

    with conn:

        conn.execute("""
            DROP TABLE banned_ip;
        """)

    createTables()
    
    conn.close()



def InsertIP_Banned(value):
    
    SetDB()
    conn = connect_to_db()
    print("BANIU: ",value)
    with conn:
        conn.execute(insert_banned, (value,))

    conn.close()
        
    return



def GetList(query_type):
    SetDB() 
    conn = connect_to_db() 
    c = conn.cursor()

    sql = ''
    
    if(query_type == 'banned'):
        sql = query_banned
    data = c.execute(sql)

    ret = []

    for row in data:
        ret.append(row[0])

    conn.close()

    return ret



def verifDB():

    conn = connect_to_db() 
    c = conn.cursor()   

    data = c.execute(sql_verif)

    if data.fetchone()[0]==1 : 
        conn.close()
        return True
    else: 
        conn.close()
        return False


# Checks table integrity in every method
def SetDB():
    if not verifDB():
        print("Generating Database...")
        createTables()




query_banned = """
        SELECT * FROM banned_ip
    """

insert_banned = 'INSERT OR REPLACE INTO banned_ip (ip_address) VALUES(?);'

sql_verif = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='banned_ip';"







