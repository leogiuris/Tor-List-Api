
import sqlite3 as sl
import json


# Method called to setup connection before any sql command
def db_connect_to_db():
    conn = sl.connect('src/database/ips_tor.db')
    return conn


# Creates 'banned_ip' Table
#   - consists of a single column containing the IP address as primary key
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


# Creates 'ip' Table (full list gathered from external sources)
#   - consists of a single column containing the IP address as the primary key
def db_CreateFullListTable():

    conn = db_connect_to_db() 

    with conn:

        conn.execute("""
            CREATE TABLE ip (
                ip_address TEXT PRIMARY KEY
            )
        """)


    conn.close()


# Inserts the full list of gathered IPs into the 'ip' table
# The SQL command eliminates the duplicates between the two sources
def db_InsertIP_FullList(ipList):

    db_SetDB()

    # Necessary so that old addresses (not present in the current set) don't persist in the database
    db_ClearFullListTable()
        
    conn = db_connect_to_db() 

    with conn:
        for el in ipList:

            conn.execute(sql_insert_full, (el,))

    conn.close()

    return


# Clears 'ip' table before inserting updated values
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
    with conn:
        conn.execute(insert_banned, (value,))

    conn.close()
        
    return



# Method called to query any table
# Returns a list of strings
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


# Verifies if tables exist
# Returns True if tables exist
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



sql_insert_full = "INSERT OR REPLACE INTO ip (ip_address) VALUES(?);"
query_banned = "SELECT * FROM banned_ip"
insert_banned = 'INSERT OR REPLACE INTO banned_ip (ip_address) VALUES(?);'
sql_verif = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='banned_ip';"
sql_verif2 = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='ip';"
query_full = "SELECT * FROM ip"





