from src.utils.external1 import *
from src.utils.external2 import *
from src.database.ipDB import *
###       BASIC INTERFACE BETWEEN THE MAIN SCRIPT AND THE DATABASE



def server_FetchFullList():
    
    if utils_CheckTime():
        data1 = utils_getIpsOnionoo()
        data2 = utils_getIpsTorNodes()
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