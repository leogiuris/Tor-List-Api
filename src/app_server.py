from src.utils.external1 import *
from src.utils.external2 import *
from src.database.ipDB import *
import json

###       BASIC INTERFACE BETWEEN THE MAIN SCRIPT AND THE DATABASE


def server_FetchFullList():
    data1 = getIpsOnionoo()
    data2 = getIpsTorNodes()
    fullList = data1+data2


    #ugly, but effectively removes duplicates
    db_InsertIP_FullList(list(set(list(fullList))))
    
    return list(db_GetList('full')) 



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