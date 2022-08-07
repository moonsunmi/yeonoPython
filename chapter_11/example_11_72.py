import urllib.parse

url = 'https://python.bakyeono.net/data/movies.json'
url_parts = urllib.parse.urlsplit(url)
print(url_parts[0])
print(url_parts[1])
print(url_parts[2])


