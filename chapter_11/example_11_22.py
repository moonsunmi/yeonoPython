countries = [
    {'name': 'China', 'population': 1403500365},
    {'name': 'Japan', 'population': 126056362},
    {'name': 'South Korea', 'population': 51736224},
    {'name': 'Pitcairn Islands', 'population': 56},
]
form = '나라: {0:16} | 인구: {1:010}'
for country in countries:
    print(form.format(country['name'], country['population']))