import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
posts = response.json()

for post in posts[:5]:
    print("Заголовок:", post["title"])
    print("Тело:", post["body"])
    print("____________________________")
