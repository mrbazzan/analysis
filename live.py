
import csv

thedict = {}
with open('Emissions.csv') as file:
    data = csv.reader(file)
    for row in data:
        thedict.setdefault(row[0], row[1:])

print('All data from Emissions.csv has been read into a dictionary.\n')
year = input('Select a year to find statistics (1997 to 2010): ')

ourlist = []
keylist = []

# Try key, value pair

for val in thedict:
    i = thedict['CO2 per capita'].index(year)
    ourlist.append(float(thedict[val][i]))
    keylist.append(val)
a = ourlist.index(max(ourlist[1:]))
b = ourlist.index(min(ourlist[1:]))


themax = keylist[a]
themin = keylist[b]
avg = sum(ourlist[1:])/len(ourlist[1:])

print(f'In {year}, countries with minimum and maximum CO2 emission levels were: [{themin}] and [{themax}] respectively.')
print(f'Average CO2 emissions in {year} were {avg: 6f}')
