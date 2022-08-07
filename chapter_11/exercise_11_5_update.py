import csv


# 인구 밀도가 높은 나라부터 낮은 나라 순으로 나라 이름과 인구 밀도를 출력하라.
def population_density(population, area):
    """인구 밀도를 구한다."""
    return population / area


with open('population.csv', 'r') as file:
    reader = csv.reader(file)
    countries = list(reader)[1:]

for country in countries:
    country.append(population_density(int(country[1]), int(country[2])))

sorted_country = sorted(countries, key=lambda row: row[3], reverse=True)

for density in sorted_country:
    print(density[0], density[3])

