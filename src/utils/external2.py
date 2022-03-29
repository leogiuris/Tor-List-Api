import requests
import time


# Since this source does not allow more than two requests every 30 minutes
# I had to come up with a Timer method so the server wouldn't ban me for making too many requests
# And for that reason I insert the response data in my database so I don't have to request every time.


# Main function in this module, returns tuple of IPs from this source to the server
def utils_getIpsTorNodes():

    data = []

    # This conditional is deprecated since the time checking is now made from the server,
    # so either its true or the method isn't called at all.
    # But I keep it for debugging purpuses.
    if(utils_CheckTime()):
        data = utils_FetchSource() 

    # As I stated above, this block of code is no longer executed.
    else:
        print("\n:( Couldn' access dan.me.uk\nLatest stored list fetched instead....\n")
        file = open('src/utils/dan.txt', 'r')
        lines = file.read()
        file.close()

        data = lines.split('\n')

    # Some items from the response are not exactly IP addresses, so I run this filter
    for el in data:
        if len(el) < 7:

            data.remove(el)


    return tuple(data)
        

# This method requests TOR IPs from an outside source and parses into a list
def utils_FetchSource():
    print("---\n\nRequest Sent\n\n---")
    data = []
    r = requests.get('https://www.dan.me.uk/torlist/')

    # Logs the time this request was made so that any get request we receive will be 
    # handled by querying the database, which is much faster.
    f = open('src/utils/timeLog.txt','w')
    f.write(str(time.time()))
    f.close()

    # this file is no longer needed, but it's helpful when debuggin.
    file = open('src/utils/dan.txt', 'w')
    file.write(str(r.text))
    file.close()

    # filtering duplicates
    for el in r.text.split('\n'):
        if el not in data:
            data.append(el)

    return data


# Opens a file with a float value representing the time the last request was sent.
# Returns True if it's been longer than 30 minutes.
def utils_CheckTime():
    with open('src/utils/timeLog.txt', 'r') as f:
        t = float(f.readline())
        f.close()
        if( time.time() - t > 1800):
            return True
        else:
            return False
