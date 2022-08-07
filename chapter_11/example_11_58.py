import json

data = [
    {
        'title': 'Interstellar',
        'genre': 'SF',
        'year': 2014,
        'starring': ['M. McConaughey', 'A. Hathaway', 'J. Chastain'],
    },
    {
        'title': 'Mary Poppins',
        'genre': 'Fantasy',
        'year': 1964,
        'starring': ['J. Andrews', 'D. Van Dyke'],
    }
]

json_data = json.dumps(data)
print(json_data)
with open('movies.json', 'w') as file:
    file.write(json_data)



