import csv

table = [
    ['title', 'genre', 'year'],
    ['Interstellar', 'SF', '2014'],
    ['Braveheart', 'Drama', '1995'],
    ['Mary Poppins', 'Fantasy', '1964'],
    ['Gloomy Sunday', 'Drama', '2000'],
]

with open('movies_output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)