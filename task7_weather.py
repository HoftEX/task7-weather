import os
import requests

api_key = os.environ.get("OPENWEATHER_KEY")
if not api_key:
    raise SystemExit("Не задана переменная окружения OPENWEATHER_KEY")

city = input("Введите название города: ")

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "appid": api_key,
    "units": "metric",
    "lang": "ru"
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"Температура в {city}: {temp} °C")
    print(f"Описание: {description}")
else:
    print("Ошибка:", data.get("message", "не удалось получить данные"))
