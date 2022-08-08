import requests

url = "http://www.xiaonengedu.com:8888/mall/file/upload"

payload={'uid': '249'}
files = {"file": ("logi.png",open("C:\\Users\\86151\\Desktop\\logo.png", "rb"),"image/png")}
headers = {
  'Cookie': '21212'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
print(response.text)
