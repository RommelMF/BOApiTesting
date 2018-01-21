# -*- coding: utf-8 -*-
import requests
import json

url = "https://bo.bars.group/bars_office/byudjeetbc/read_rows/"

querystring = {"_dc":"1516431737660"}

payload = "{\"extraParams\":{},\"filters\":[],\"additionalParams\":{}}"
headers = {
    'origin': "https://bo.bars.group",
    'x-requested-with': "XMLHttpRequest",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    'content-type': "application/json; charset=UTF-8",
    'accept': "*/*",
    'referer': "https://bo.bars.group/",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    'cookie': "",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)


# conversion to dict type
d1 = dict(response.json())
print(d1["byudjeetbc"][0]["bc__kagoriyabc__name"])
print(d1["byudjeetbc"][0]["bc__name"])
list_bc_name = ""
i = 0
for i in range(len(d1["byudjeetbc"])):
   list_bc_name = list_bc_name + "\n " + d1["byudjeetbc"][i]["bc__name"]
print (list_bc_name)
print(response.status_code)
print