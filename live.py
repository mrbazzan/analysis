
import csv
import matplotlib.pyplot as plt

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

# Get the index of the year
i = thedict['CO2 per capita'].index(year)

for val in thedict:
    # store the value of index i for each key in ourlist
    ourlist.append(float(thedict[val][i]))
    keylist.append(val)

# Get the index of the maximum and minimum value in ourlist
a = ourlist.index(max(ourlist[1:]))
b = ourlist.index(min(ourlist[1:]))

# return the country
themax = keylist[a]
themin = keylist[b]
avg = sum(ourlist[1:])/len(ourlist[1:])

print(f'In {year}, countries with minimum and maximum CO2 emission levels were: [{themin}] and [{themax}] respectively.')
print(f'Average CO2 emissions in {year} were {avg:6f}')

country = input('Select the country to visualize: ').title()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

# set the labels for the figure
ax.set_xticklabels(thedict['CO2 per capita'], rotation=30, fontsize='small')
props = {
    'title': 'Year VS Emissions in Capita',
    'xlabel': 'Year',
    'ylabel': f'Emissions in {country}',
}
ax.set(**props)

# plot the graph
plt.plot(list(map(lambda x: float(x), thedict[country])))
plt.show()
