import requests
import json

query = input("What type of news are interested in?")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-02-13&sortBy=publishedAt&apiKey=5abd0877f2934bba998508bf41086bc4"
r = requests.get(url)
news = json.loads(r.text)
# print(news,type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("-------------------------------------------------")