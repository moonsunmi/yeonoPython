import urllib.parse

url = 'https://python.bakyeono.net/data/movies.json'
url_parts = urllib.parse.urlsplit(url)
url_parts = list(url_parts)
url_parts[2] = '/chapter-11.html'
print(urllib.parse.urlunsplit(url_parts))
