import csv
from pathlib import Path
import random

path = Path.cwd() / 'data' / 'data_2.csv'
with open(path, 'r') as f:
    data = list(csv.reader(f))
data.pop(0)
names = [row[0] for row in data]
cities = set([row[1] for row in data])
cart = [0, 1]
file = []
string = []
name_iter = (name for name in names)
for name in name_iter:
    city_iter = (city for city in cities)
    for city in city_iter:
        x_iter = (x for x in cart)
        for bool in x_iter:
            string = [name, city, bool, random.randint(0, 1), random.randint(0, 1)]
            print(string)
            file.append(string)
print(len(file))
path_to_result_file = Path.cwd() / 'data' / 'results.csv'
with open(path_to_result_file, 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for line in file:
        writer.writerow(line)

