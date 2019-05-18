import requests
import hmac
import hashlib
import base64
import time
import random
import re


appid = "1258380689"
bucket = "" #参考本文开头提供的链接
secret_id = "AKIDEMFxSnNsa8RWNzK2Selon6JRXWGrLNAt"  #参考官方文档
secret_key = "sZ2HTSBNMCrIWbWFo9IDwQhldQ1Xu4zn"  #同上
expired = time.time() + 2592000
onceExpired = 0
current = time.time()
rdm = ''.join(random.choice("0123456789") for i in range(10))


info = "a=" + appid + "&b=" + bucket + "&k=" + secret_id + "&e=" + str(expired) + "&t=" + str(current) + "&r=" + str(rdm) + "&u=0&f="

signindex = hmac.new(bytes(secret_key,'utf-8'),bytes(info,'utf-8'), hashlib.sha1).digest()  # HMAC-SHA1加密
sign = base64.b64encode(signindex + bytes(info,'utf-8'))  # base64转码，也可以用下面那行转码
#sign=base64.b64encode(signindex+info.encode('utf-8'))

f = open(r'./images/2.jpg', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())

url = "https://recognition.image.myqcloud.com/ocr/invoice"
headers = {"Host": 'recognition.image.myqcloud.com',
           "Authorization": sign
           }


files = {'appid': (None,appid),'image': img}

r = requests.post(url, files=files, headers=headers)

responseinfo = r.content
data = responseinfo.decode('utf-8')
print(data)
r_index = r'itemstring":"(.*?)"'  # 做一个正则匹配
result = re.findall(r_index, data)
for i in result:
    print(i)
