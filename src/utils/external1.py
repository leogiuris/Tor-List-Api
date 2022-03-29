
import requests
import json


def utils_getIpsOnionoo():

    # This source returns a JSON object sometimes with multiple IPv6 addresses for a single IPv4 address
    r = requests.get('https://onionoo.torproject.org/summary?limit=5000')

    r_parsed = json.loads(r.text)['relays']
    data = []

    # this method separates those addresses and appends them on a list as a single item
    for el in r_parsed:
        data.append(el['a'][0])
        
        if (len(el['a']) > 1):
            data.append(el['a'][1].replace('[','').replace(']',''))


    return tuple(data)




