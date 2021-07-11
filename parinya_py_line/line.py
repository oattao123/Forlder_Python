import requests
url = 'https://notify-api.line.me/api/notify'
token = 'RUjke7gbmMZUTyFX9VaFiIumQdpHX5GyZj2S7DV04Sb'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg = 'Data TMD Ready'
a = requests.post(url,headers=headers,data = {'message':'Hello'})
print(a.text)