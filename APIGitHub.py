import requests
import database

res = requests.get('https://api.github.com/search/repositories?q=stars%3A%3E0&sort=stars&order=desc&page=1&per_page=5')

print(res.json())


