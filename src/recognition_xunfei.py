#-*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import json
import os
URL = "http://webapi.xfyun.cn/v1/service/v1/ocr/invoice"
APPID = "5cd83152"
API_KEY = "7c8b080b96e7f0dc3a21fa42d051285b"

def getHeader():
    curTime = str(int(time.time()))
    param = {"engine_type": "invoice"}
    param = json.dumps(param)
    #x_param = base64.b64encode(param.encode('utf-8'))
    #param = "{\"auto_rotate\":\"true\"}"
    paramBase64 = base64.b64encode(param.encode('utf-8'))

    m2 = hashlib.md5()
    str1 = API_KEY + curTime + str(paramBase64,'utf-8')
    m2.update(str1.encode('utf-8'))
    checkSum = m2.hexdigest()

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header


img_path = "./images/"
output_path = "output/20190513.txt"
fo = open(output_path, "w")

for file_name in os.listdir(img_path):
    with open(img_path + file_name, 'rb') as f:
        f1 = f.read()
    f1_base64 = str(base64.b64encode(f1), 'utf-8')
    data = {'image': f1_base64}

    #headers=getHeader(language, location)
    r = requests.post(URL, data=data, headers=getHeader())
    result = str(r.content, 'utf-8')
    data = json.loads(result, encoding="utf-8")["data"]
    print(data)
    print(data["vat_invoice_goods_list"].split("\n"))
    print(data["vat_invoice_electrans_quantity"].split("\n"))
    if data.__contains__("vat_invoice_electrans_unit"):
        print(data["vat_invoice_electrans_unit"].split("\n"))
    print(data["vat_invoice_electrans_unit_price"].split("\n"))
    print(data["vat_invoice_price_list"].split("\n"))
    print(data["vat_invoice_tax_list"].split("\n"))

    print("\n")

