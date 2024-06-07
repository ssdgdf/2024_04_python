import requests

apikeys = "b5d11db6362382d0d9b983c007cc444a"
lat = 37.491
lon = 126.72
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikeys}"

response = requests.get(url)
data = response.json()
print(data)