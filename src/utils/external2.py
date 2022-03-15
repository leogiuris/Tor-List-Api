


import requests
import json
import time



def getIpsTorNodes():

    data = []

    if(checkTimer()):
        data = FetchSource()

    else:
        print("Couldn' access dan.me.uk\nLatest stored list fetched instead....")
        file = open('src/utils/dan.txt', 'r')
        lines = file.readlines()
        
        for line in lines:
            if line.replace('\n','') in data:
                data.append(line.replace('\n',''))
        
    print(*data[0:10], sep = '\n')
    return tuple(data)
        


def checkTimer():

    with open('src/utils/timeLog.txt', 'r') as f:
        t = float(f.readline())
        f.close()
        if( time.time() - t > 1800):
            return True
        else:
            return False



def FetchSource():
    print("ACESSOU")
    data = []
    r = requests.get('https://www.dan.me.uk/torlist/?exit')
    f = open('src/utils/timeLog.txt','w')
    f.write(str(time.time()))
    f.close()

    # danf = open('src/utils/dan.txt', 'w', buffering=1)
    # print("tamanho (dan): ", len(r.text))
    # danf.write(r.text)
    # danf.close()
    
    for el in r.text:
        if el not in data:
            data.append(el)
    return data


