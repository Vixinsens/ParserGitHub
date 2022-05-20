import requests
import datetime
from database import DataBase



repo_number = 10

res = requests.get(f'https://api.github.com/search/repositories?q=stars%3A%3E0&sort=stars&order=desc&per_page={repo_number}')


json = res.json()

database = DataBase(
    host='localhost',
    port=27017,
    db='github',
    collection='repos')


for repo in json['items']:
    data = {'name': repo['full_name'], 'url': repo['html_url'], 'stars': repo['stargazers_count'], 'date': datetime.datetime.now()}
    print(data)
    database.insert_one(data)
