from src.utils.external1 import *
from src.utils.external2 import *
from src.database.ipDB import *
import json

###       BASIC INTERFACE BETWEEN THE MAIN SCRIPT AND THE DATABASE


def FetchFullList():
    data1 = getIpsOnionoo()
    data2 = getIpsTorNodes()
    fullList = data1+data2

    db_InsertIP_FullList(fullList)

    return list(set(list(fullList))) #ugly but effectively removes duplicates



def BanIP(data):
    db_SetDB()
    db_InsertIP_Banned(data)
    return



def FetchValidList():
    fetch = db_GetList('full')
    if(len(fetch) < 1):
        view = FetchFullList()
    else:
        view = fetch
    for address in db_GetList('banned'):
        print(address)
        try:
            view.remove(address)
        except:
            print(address + ": Ip not in list")
    return view



