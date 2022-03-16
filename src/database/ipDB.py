
import sqlite3 as sl
import json

def db_connect_to_db():
    conn = sl.connect('src/database/ips_tor.db', check_same_thread=False)
    return conn



def db_createBannedTable():

    conn = db_connect_to_db() 
    
    with conn:

        conn.execute("""
            CREATE TABLE banned_ip (
                ip_address TEXT PRIMARY KEY
            )
        """)

    print("tabelas criadas")

    conn.close()



def db_CreateFullListTable():

    conn = db_connect_to_db() 

    with conn:

        conn.execute("""
            CREATE TABLE ip (
                ip_address TEXT PRIMARY KEY
            )
        """)


    conn.close()



def db_InsertIP_FullList(ipList):

    db_SetDB()

    db_ClearFullListTable()
        
    conn = db_connect_to_db() 

    with conn:
        for el in ipList:
            if(type(el) == list):
                el = el[0]
            conn.execute("INSERT OR REPLACE INTO ip (ip_address) VALUES(?);", (el,))

    conn.close()

    return



def db_ClearFullListTable():
    conn = db_connect_to_db() 

    with conn:

        conn.execute('DELETE FROM ip;')

    conn.close()
    
    pass



def db_DropFullList():
    db_SetDB()
    conn = db_connect_to_db() 

    with conn:

        conn.execute("""
            DROP TABLE ip;
        """)

    db_createBannedTable()
    
    conn.close()



def db_DropALL():

    db_SetDB()
    conn = db_connect_to_db() 

    with conn:

        conn.execute("""
            DROP TABLE banned_ip;
        """)
        conn.execute("""
            DROP TABLE ip;
        """)

    db_createBannedTable()
    
    conn.close()



def db_InsertIP_Banned(value):
    
    db_SetDB()
    conn = db_connect_to_db()
    print("BANIU: ",value)
    with conn:
        conn.execute(insert_banned, (value,))

    conn.close()
        
    return



def db_GetList(query_type):
    db_SetDB() 
    conn = db_connect_to_db() 
    c = conn.cursor()

    if(query_type == 'banned'):
        data = c.execute(query_banned)
    elif(query_type == 'full'):
        data = c.execute(query_full)

    ret = []

    for row in data:
        ret.append(row[0])

    conn.close()

    return ret



def db_verifDB():

    conn = db_connect_to_db() 
    c = conn.cursor()   

    data = c.execute(sql_verif)

    if (data.fetchone()[0]==1): 
        conn.close()
        return True
    else: 
        conn.close()
        return False


# Checks table integrity in every method
def db_SetDB():
    if not db_verifDB():
        print("Generating Database...")
        db_createBannedTable()
        db_CreateFullListTable()




query_banned = "SELECT * FROM banned_ip"
insert_banned = 'INSERT OR REPLACE INTO banned_ip (ip_address) VALUES(?);'
sql_verif = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='banned_ip';"
sql_verif2 = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='ip';"
query_full = "SELECT * FROM ip"





