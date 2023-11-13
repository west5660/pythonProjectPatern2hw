import requests

url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

headers = {
	"accept": "application/json",
	"X-RapidAPI-Key": "ebc68c4adcmshb044d2fcb5ccd85p1ea4aajsn8569bb3a3117",
	"X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
print(response)
print(response.json())
data = response.json()
print(data['value'])

######################################################################

import requests

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

payload = {
	"q": data['value'],
	"target": "ru",
	"source": "en"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "ebc68c4adcmshb044d2fcb5ccd85p1ea4aajsn8569bb3a3117",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
data  = response.json()
# print(data['data']['translations'][0]['translatedText'])

#############################

url = "https://imdb188.p.rapidapi.com/api/v1/getWeekTop10"

headers = {
	"X-RapidAPI-Key": "ebc68c4adcmshb044d2fcb5ccd85p1ea4aajsn8569bb3a3117",
	"X-RapidAPI-Host": "imdb188.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())


