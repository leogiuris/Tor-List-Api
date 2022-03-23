import requests
import time


def utils_getIpsTorNodes():

    data = []

    if(utils_CheckTime()):
        data = utils_FetchSource()

    else:
        print("\n:( Couldn' access dan.me.uk\nLatest stored list fetched instead....\n")
        file = open('src/utils/dan.txt', 'r')
        lines = file.read()
        file.close()

        data = lines.split('\n')

    for el in data:
        if len(el) < 5:

            data.remove(el)

    return tuple(data)
        


def utils_FetchSource():
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



def utils_CheckTime():
    with open('src/utils/timeLog.txt', 'r') as f:
        t = float(f.readline())
        f.close()
        if( time.time() - t > 1800):
            return True
        else:
            return False
