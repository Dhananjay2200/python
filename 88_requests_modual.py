import requests
from bs4 import BeautifulSoup
url = "https://www.arthurrump.com/project/fake-staticgen/"
r = requests.get(url)
# print(r.text)
soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)
# url = "https://jsonplaceholder.typicode.com/posts"
# r = requests.get(url)
# data = {
#     "userId": 1,
#     "it": 1,
#     "title": "are or do repels provide blacked out except option criticizes",
#     "body": "because he also accepts\nundertakes the consequences of refusal and when\nhe criticizes the troubles so that the whole\nof our things are but they are the matter will happen to the architect"
# }
# headers = {
#     'Content-type':
# 'application/json; charset=UTF-8',
# }
# response = requests.post(url,headers = headers,json = data)

# print(response.text)