import csv
import pprint

with open('movies.csv') as file:
    reader = csv.reader(file)
    movies = list(reader)

pprint.pprint(movies)