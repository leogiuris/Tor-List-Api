


import json
import requests


BASE = "http://localhost:5000/"



resp1 = (requests.get(BASE + "fullList")).json()

resp2a = (requests.post(BASE + "ban_ip", json = {'ip':resp1[0]})).json()
resp2b = (requests.post(BASE + "ban_ip", json = {'ip':resp1[1]})).json()
# resp2c = (requests.post(BASE + "ban_ip", json = {'ip':resp1[2]})).json()
# resp2d = (requests.post(BASE + "ban_ip", json = {'ip':resp1[3]})).json()
# resp2e = (requests.post(BASE + "ban_ip", json = {'ip':resp1[4]})).json()

resp3 = (requests.get(BASE + "validList")).json()





print("\nFULL LIST: ", len(resp1),"\n")
print(*resp1[0:6], sep = '\n')

print("....\n\nBanned 2 more ip addresses... ")

print("\n\nVALID ONLY LIST: ", len(resp3),"\n")
print(*resp3[0:6], sep = '\n')

print("....\n\n")



