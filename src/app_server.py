from utils.external1 import *
from utils.external2 import *
from database.ipDB import *
import json



def PopulateDB():

    #drops all tables to make sure all ips came from the latest fetch
    DropALL()   

    data = getIpsOnionoo()
    data2 = getIpsTorNodes()

    InsertIP_List(data+data2)
    return


def FetchFullList():
    data1 = getIpsOnionoo()
    data2 = getIpsTorNodes()
    return list(data1+data2)



# def FetchFullList():
#     return GetList('full')



def BanIP(data):
    SetDB()
    InsertIP_Banned(data)
    return



def FetchValidList():
    view = FetchFullList()
    for address in FetchBannedList():
        print(address)
        try:
            view.remove(address)
        except:
            print(address + ": Ip not in list")
    return view



def FetchBannedList():
    return GetList('banned')



#PopulateDB()