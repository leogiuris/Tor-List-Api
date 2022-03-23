from src.utils.external1 import *
from src.utils.external2 import *
from src.database.ipDB import *
###       BASIC INTERFACE BETWEEN THE MAIN SCRIPT AND THE DATABASE AND EXTERNAL SOURCES


# This module

# Requests the IP addresses from two external APIs 
# If it's been less than 30 minutes then the server will fetch directly from the database
# Returns the full list of addresses without duplicates
def server_FetchFullList():
    
    if utils_CheckTime(): # returns true if more than 30 minutes have passed
        data1 = utils_getIpsOnionoo()  
        data2 = utils_getIpsTorNodes()

        print(len(data1), " entries from https://onionoo.torproject.org/summary?limit=5000")  
        print(len(data2), " entries from https://www.dan.me.uk/torlist/") 

        # a way to remove duplicates and return the original list without having to query the database and get the same list
        fullList = list(set(list(data1+data2))) 
        db_InsertIP_FullList(fullList)
    else:
        fullList = db_GetList('full')
    
    return fullList


# inserts IP addresses into the database, plain and simple
def server_BanIP(data):
    db_InsertIP_Banned(data)
    return


# Returns list of all addresses that are not in the banned_ip table
def server_FetchValidList():

    data = db_GetList('full')

    if(len(data) < 1): # if the database is still empty
        view = server_FetchFullList()
    else:
        view = data

    for address in db_GetList('banned'):
        try:
            view.remove(address)
        except:
            print(address + ": Ip not in list")

    return view


# returns a list of banned addresses
def server_getBannedList():
    return db_GetList('banned')