import requests

key = 'ffba57f44fa1889286e1e5a405e4e879'
zapros = 'https://api.openweathermap.org/data/2.5/weather'
id = 504341
try:
    result = requests.get(zapros,params={'id':id, 'lang':'ru','units':'metric', 'appid':key})
    print(result)
    data=result.json()
    print(data)
    k1=data.get('name')
    k2=str(round(data['main']['temp'],1))+'C'
    k3=str(data['wind']['speed'])+'m/c'
    k4 = data['weather'][0]['description']
    print(k1,k2,k3,k4)
except:
    print('ne ok')

zapros = 'https://api.openweathermap.org/data/2.5/forecast'
result = requests.get(zapros,params={'id':id, 'lang':'ru','units':'metric', 'appid':key})
print(result)
data = result.json()
print(data)
for i in data['list']:
    if i['dt_txt'][11:13]=='15':
        print(i['main']['temp'],i['weather'][0]['description'],i['dt_txt'])
