# coding:utf-8

import base64
import urllib.request
import urllib.parse
import json
import os

access_token = '24.a08ac6199e56544d08a977e779fa72ea.2592000.1557749001.282335-16011906'
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/vat_invoice?access_token=' + access_token

img_path = "./images/"
output_path = "output/20190513.txt"
fo = open(output_path, "w")

for file_name in os.listdir(img_path):
    # 二进制方式打开图文件
    f = open(img_path + file_name, 'rb')
    # 参数image：图像base64编码
    img = base64.b64encode(f.read())
    params = {"image": img}
    params = urllib.parse.urlencode(params).encode("utf-8")
    request = urllib.request.Request(url, params)
    request.add_header('Content-Type', 'application/x-www-form-urlencoded')
    response = urllib.request.urlopen(request)
    content = response.read()
    print(content.decode("utf-8"))
    words_result = json.loads(content, encoding="utf-8")["words_result"]

    commodity_name = [x["word"] for x in words_result["CommodityName"]]
    commodity_num = [x["word"] for x in words_result["CommodityNum"]]
    commodity_unit = [x["word"] for x in words_result["CommodityUnit"]]
    cmmodity_amount = [x["word"] for x in words_result["CommodityAmount"]]
    commodity_tax = [x["word"] for x in words_result["CommodityTax"]]
    commodity_price = [x["word"] for x in words_result["CommodityPrice"]]
    fo.write("图片名称：" + file_name + "\n")
    fo.write("名称：" + "，".join(commodity_name) + "\n")
    fo.write("数量：" + "，".join(commodity_num) + "\n")
    fo.write("单位：" + "，".join(commodity_unit) + "\n")
    fo.write("单价：" + "，".join(commodity_price) + "\n")
    fo.write("金额：" + "，".join(cmmodity_amount) + "\n")
    fo.write("税额：" + "，".join(commodity_tax) + "\n")

    fo.write("\n")
    print(commodity_name)
    print(commodity_num)
    print(commodity_unit)
    print(cmmodity_amount)
    print(commodity_tax)
    print(commodity_price)

fo.close()
