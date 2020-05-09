
import csv
import matplotlib.pyplot as plt

the_dict = {}
with open('Emissions.csv') as file:
    data = csv.reader(file)
    for row in data:
        the_dict.setdefault(row[0], row[1:])

print('All data from Emissions.csv has been read into a dictionary.\n')

while True:
    try:

        year = input('Select a year to find statistics (1997 to 2010): ')

        our_list = []
        key_list = []

        # Get the index of the year
        i = the_dict['CO2 per capita'].index(year)

        for key, value in the_dict.items():
            # store the value of index i for each key in our_list
            our_list.append(float(value[i]))
            key_list.append(key)

        # Get the index of the maximum and minimum value in our list
        a = our_list.index(max(our_list[1:]))
        b = our_list.index(min(our_list[1:]))

        # return the country
        the_max = key_list[a]
        the_min = key_list[b]
        avg = sum(our_list[1:]) / len(our_list[1:])

        print(f'\nIn {year}, countries with minimum and maximum CO2 emission '
              f'levels were: [{the_min}] and [{the_max}] respectively.')
        print(f'Average CO2 emissions in {year} were {avg:6f}\n')
        break
    except ValueError:
        print('Sorry that is not a valid Year.')

while True:

    country = input('Select the country to visualize: ').title()
    if country not in key_list:
        print('Sorry this is not a valid Country')
        continue

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # set the labels for the figure
    ax.set_xticklabels(the_dict['CO2 per capita'], rotation=30, fontsize='small')
    props = {
        'title': 'Year VS Emissions in Capita',
        'xlabel': 'Year',
        'ylabel': f'Emissions in {country}'
    }
    ax.set(**props)
    # plot the graph
    plt.plot(list(map(lambda x: float(x), the_dict[country])), label=f'{country}')
    plt.legend()
    plt.show()
    break

while True:
    try:
        two_country = input('\nWrite two comma-separated countries for which you '
                            'want to visualize data(country_a, country_b): ').title().split(', ')

        # get the two values entered into two separate variables.
        count_a, count_b = two_country
        plt.plot(list(map(lambda x: float(x), the_dict[count_a])), label=f'{count_a}')
        plt.plot(list(map(lambda x: float(x), the_dict[count_b])), 'k--', label=f'{count_b}')
        plt.legend()
        plt.show()
        break
    except ValueError:
        print('Please enter up to two comma-separated countries for which you want to visualize...')

    except KeyError:
        print('Sorry that is not a valid Country')


while True:
    try:
        three_country = input('\nWrite up to three comma-separated countries'
                              ' for which you want to extract data: ').title()
        the_cont = three_country.split(', ')
        if len(the_cont) > 3:
            print('ERR: Sorry, at most 3 countries can be entered.')
        with open('Emissions_subset.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file)
            the_dict['CO2 per capita'].insert(0, 'CO2 per capita')
            csv_writer.writerow(the_dict['CO2 per capita'])
            for cont in the_cont:
                the_dict[cont].append(cont)
                the_dict[cont].insert(0, cont)
                csv_writer.writerow(the_dict[cont])
        print(f'Data successfully extracted for countries {three_country} saved into file Emissions_subset.csv')
        break
    except KeyError:
        print(f'Sorry "{cont}" is not a valid country')
