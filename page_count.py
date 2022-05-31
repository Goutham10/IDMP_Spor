import requests
import json
from requests.auth import HTTPBasicAuth
import oauth2

# def login(username, password):
#     s = requests.Session()
#     payload = {
#         "username" : username,
#         "password" : password,
#     }
#     res = requests.post("https://login.ema.europa.eu/oam/server/auth_cred_submit",json=payload)
#     s.headers.update({"authorization": json.loads(res.content)['token']})
#     print(res.content)
#     return s

# session = login("boine_g", "Goutham@idmp10")
# print(session.cookies)
# # r = session.patch("https://spor.ema.europa.eu/v1/lists?pagesize=500")
# print(r.content)

headers = {
    "accept" : "application/json"
}

# res = requests.get("https://login.ema.europa.eu/oam/server/auth_cred_submit", 
#                    auth=('boine_g','Goutham@idmp10'), headers=headers)
# print(res.request.headers.keys())


# session = requests.Session()
# res = session.get("https://spor.ema.europa.eu/sporwi/")
# print(res.cookies.get_dict())



url = "https://login.ema.europa.eu/oamreauthenticate?redirect_url=https://spor.ema.europa.eu/rmswi/"
# url = "https://login.ema.europa.eu/oam/server/auth_cred_submit"

# url = "https://spor.ema.europa.eu/rmswi/"
payload = {
    "username" : "boine_g",
    "password" : "Goutham@idmp10",
    "submit" : "Login"
}

resp = requests.get(url= url, data=payload,allow_redirects=True)
# print(resp.url)
site1 = resp.url



resp1 = requests.get(url= site1, data=payload,allow_redirects=True)
site2 = resp1.url
print(site2)

resp2 = requests.get(url= site2, data=payload,allow_redirects=True,)
# print(resp2.url)

# print(resp.text)


# resp = requests.get(url= url)
# print(resp.cookies.get_dict())