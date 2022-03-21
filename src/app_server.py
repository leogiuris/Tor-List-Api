from src.utils.external1 import *
from src.utils.external2 import *
from src.database.ipDB import *
###       BASIC INTERFACE BETWEEN THE MAIN SCRIPT AND THE DATABASE





# returns true if it's been 30 minutes since last outside API get



def server_FetchFullList():
    
    if CheckTime():
        data1 = getIpsOnionoo()
        data2 = getIpsTorNodes()
        fullList = list(set(list(data1+data2)))
        db_InsertIP_FullList(fullList)
    else:
        fullList = db_GetList('full')
    

    return fullList



def server_BanIP(data):
    db_SetDB()
    db_InsertIP_Banned(data)
    return




def server_FetchValidList():
    fetch = db_GetList('full')
    if(len(fetch) < 1):
        view = server_FetchFullList()
    else:
        view = fetch
    for address in db_GetList('banned'):
        try:
            view.remove(address)
        except:
            print(address + ": Ip not in list")
    return view


def server_getBlacklist():
    return db_GetList('banned')