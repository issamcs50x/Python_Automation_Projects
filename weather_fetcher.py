import requests

API_KEY = "92c7c442ee683dd09a8533bc174f7914"

city = input("enter the city: ").strip().lower()

URL = f"https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    description = data.get("weather")[0].get("description")
    temp = data.get("main").get("temp")
    infos = {"description": description, "temp": temp}
    print(infos)
else:
    print("Something goes wrong!")
