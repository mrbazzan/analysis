
import csv

thedict = {}
with open('Emissions.csv') as file:
    data = csv.reader(file)
    for row in data:
        thedict.setdefault(row[0], row[1:])
for key, value in thedict.items():
    print(f'{key} - {value}')
