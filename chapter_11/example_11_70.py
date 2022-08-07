import urllib.request

url = 'https://python.bakyeono.net/data/movies.json'
text_data = urllib.request.urlopen(url).read().decode('-utf-8')
print(text_data)