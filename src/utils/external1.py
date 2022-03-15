
import requests
import json

def getIpsOnionoo():
    
    r = requests.get('https://onionoo.torproject.org/summary?limit=5000')

    r_parsed = json.loads(r.text)['relays']
    data = []

    for el in r_parsed:

        aux = list(el['a'])
        if (len(aux) > 1):

            aux[1] = str(aux[1]).replace('[','').replace(']','')

        data.append(aux)


    return tuple(data)




