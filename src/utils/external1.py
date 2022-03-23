
import requests
import json


def utils_getIpsOnionoo():
    
    r = requests.get('https://onionoo.torproject.org/summary?limit=5000')

    r_parsed = json.loads(r.text)['relays']
    data = []

    for el in r_parsed:
        data.append(el['a'][0])
        
        if (len(el['a']) > 1):
            data.append(el['a'][1].replace('[','').replace(']',''))


    return tuple(data)




