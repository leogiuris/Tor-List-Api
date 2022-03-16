


import requests
import json
import time



def getIpsTorNodes():

    data = []

    if(checkTimer()):
        data = FetchSource()

    else:
        print("\n:( Couldn' access dan.me.uk\nLatest stored list fetched instead....")
        file = open('src/utils/dan.txt', 'r')
        lines = file.readlines()
        file.close()
        for line in lines:
            if line.replace('\n','') in data:
                data.append(line.replace('\n',''))
    
    

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
    print("---\n\nACESSOU\n\n---")
    data = []
    r = requests.get('https://www.dan.me.uk/torlist/?exit')
    f = open('src/utils/timeLog.txt','w')
    f.write(str(time.time()))
    f.close()

    print(r.text[0:50])

    for el in r.text.split('\n'):
        if el not in data:
            data.append(el)
    
    print(len(data))
    #print(*data[0:20], sep = '\n')
    return data


