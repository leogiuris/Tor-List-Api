from utils.external1 import *
from utils.external2 import *
from database.ipDB import *
import json


def PopulateDB():
    DropALL()
    data = getIpsOnionoo()
    data2 = getIpsTorNodes()

    InsertIP_List(data+data2)
    return



def FetchFullList():
    return GetList('full')


def BanIP(data):
    InsertIP_Banned(data)
    return



def FetchValidList():
    return GetList('valid')



def FetchBannedList():
    return GetBannedList()



PopulateDB()