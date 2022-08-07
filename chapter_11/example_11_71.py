import urllib.request
import json

url = 'https://python.bakyeono.net/data/movies.json'
text_data = urllib.request.urlopen(url).read().decode('-utf-8')
movies = json.loads(text_data)
sorted_by_year = sorted(movies, key=lambda movie: movie['year'])

for movie in sorted_by_year:
    print(str(movie['year']) + ' ' + movie['title'].upper())