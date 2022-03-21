


import requests
import time




def getIpsTorNodes():

    data = []

    if(CheckTime()):
        data = FetchSource()

    else:
        print("\n:( Couldn' access dan.me.uk\nLatest stored list fetched instead....\n")
        file = open('src/utils/dan.txt', 'r')
        lines = file.read()
        file.close()
        # for line in lines:
        #     if line.replace('\n','') in data:
        #         data.append(line.replace('\n',''))

        data = lines.split('\n')

    for el in data:
        if len(el) < 5:
            print("<entrada invalida>: ", el)
            data.remove(el)

    return tuple(data)
        

def FetchSource():
    print("---\n\nACESSOU\n\n---")
    data = []
    r = requests.get('https://www.dan.me.uk/torlist/')
    f = open('src/utils/timeLog.txt','w')
    f.write(str(time.time()))
    f.close()

    file = open('src/utils/dan.txt', 'w')
    file.write(str(r.text))
    file.close()

    for el in r.text.split('\n'):
        if el not in data:
            data.append(el)

    return data


def CheckTime():
    with open('src/utils/timeLog.txt', 'r') as f:
        t = float(f.readline())
        f.close()
        if( time.time() - t > 1800):
            return True
        else:
            return False
