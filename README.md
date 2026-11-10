# task7-weather
weather homework


Скрипт отправляет GET-запрос к публичному API JSONPlaceholder
и выводит заголовки и тела первых 5 постов.

## Файл

`task7_posts.py`

## Что делает

1. Отправляет GET-запрос к `https://jsonplaceholder.typicode.com/posts`.
2. Получает список постов в формате JSON.
3. Берёт первые 5 постов.
4. Выводит для каждого заголовок (`title`) и тело (`body`).

## Запуск

Установите зависимость:

bash
pip install requests



`task7_weather.py` — принимает название города, отправляет GET-запрос к OpenWeather
и выводит текущую температуру и описание погоды.

Ключ API не хранится в репозитории. 


!!!!Перед запуском задайте переменную окружения!!!!!
`OPENWEATHER_KEY`:

- Windows (cmd): `set OPENWEATHER_KEY=ваш_ключ`
- Windows (PowerShell): `$env:OPENWEATHER_KEY="ваш_ключ"`
- macOS/Linux: `export OPENWEATHER_KEY=ваш_ключ`

Получить ключ: https://openweathermap.org/api

Запуск:
bash
pip install requests
python task2_weather.py
