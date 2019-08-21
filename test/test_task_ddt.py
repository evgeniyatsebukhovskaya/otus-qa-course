import csv
from pathlib import Path
from itertools import product, islice

path = Path.cwd() / 'data' / 'data_2.csv'
with open(path, 'r') as f:
    data = list(csv.reader(f))

names = set()
cities = set()
credit_cards = set()
vklad = set()
ipoteka = set()

for row in data[1:]:
    names.add(row[0][0:-1])
    cities.add(row[1])
    credit_cards.add(row[2])
    vklad.add(row[3])
    ipoteka.add(row[4])

for s in (names, cities, credit_cards, vklad, ipoteka):
    s.discard('')

combinations = islice(product(names, cities, credit_cards, vklad, ipoteka), 100)
file = list(combinations)

path_to_result_file = Path.cwd() / 'data' / 'results.csv'
with open(path_to_result_file, 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for line in file:
        writer.writerow(line)
