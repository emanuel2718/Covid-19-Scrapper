#!/usr/bin/env python

# Author: by Emanuel Ramirez on March 15, 2020
# Date: March 15, 2020

from matplotlib import pyplot
from pydoc import pager
from time import sleep
import argparse
import datetime as dt
import json
import matplotlib
import pandas as pd
import requests
import seaborn
import sys
import yaml



def main():
    ''' Simple web scraping script to get covid-19 data using:
    https://thevirustracker.com free API.
    '''

    if len(sys.argv) == 2:

        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            parser = argparse.ArgumentParser(
                description='''COVID Scrapper v0.0.2''',
                epilog='''Thanks for using our service.''')

            parser.add_argument('-w', help='Print Worldwide COVID-19 data')
            parser.add_argument('-g', help='Plot COVID-19 data')
            parser.add_argument('-list',
                        help='Print a list of available countries and codes')
            parser.add_argument('-s', metavar='[country]',
                        help='Print specific country COVID-19 data')
            args = parser.parse_args()

        if sys.argv[1] == '-w':
            get_worldwide_stats(WORLDWIDE_URL)
            sys.exit(0)

        elif sys.argv[1] == '-list':
            print_list_to_user()
            sys.exit(0)

        elif sys.argv[1] == '-g':
            prep_data()
            sys.exit(0)

    elif len(sys.argv) > 2:
        # Account for countries with spaces (i.e United States)
        string = ""
        index = 2

        while index < len(sys.argv):
            if sys.argv[index] != " ":
                string += sys.argv[index] + " "
                index += 1

        string = string.strip()
        # This acts as if the user chose option #3 in the menu.
        country = 'https://thevirustracker.com/free-api?countryTotal={}'\
            .format(get_country_code(string))

        get_country_stats(country)

    else:
        # No cli-arguments given.
        menu_driver()

def menu_driver():
    """Program main driver.

    The user can choose between 1-4 menu options.
    1. Wordwide stats
    2. List of countries
    3. Specific country stats (Full country or two-letter code)
    4. Exit the program
    """

    done = False
    while not done:
        print_menu()
        user_input = input("Please, enter option: ")
        print('------------------------------------------------')
        option_info = check_validity(user_input)
        if option_info != -1:
            pass
            if option_info == 5:
                done = True
                print("\n")
                print("Thank you for using COVID-19 Scrapper. Stay safe!")
            else:
                evaluate_option(option_info)
        else:
            print("Please, enter a valid number option from 1 to 4....")
            sleep(2)
            print('------------------------------------------------')

def print_menu():
    """Prints the menu to the user."""

    # TODO: think about plotting option in menu.
    print()
    print("COVID-19 Stats Scrapper. Please, select a number." + "\n")
    print("1. To see worldwide stats.")
    print("2. To see a list of the available countries and their"\
          + " respective abbreviations.")

    print("3. To type a country or abrreviation and see their stats.")
    print("4. To visualize Total Cases in the most infected countries.")
    print("5. Exit")

def check_validity(option):
    """Check if the input received is a valid digit 1 to 4 inclusive."""

    if option.isdigit():
        numeric_option = int(option)
        if numeric_option >=1 and numeric_option <= 5:
            return numeric_option
        else:
            return -1
    else:
        return -1


def evaluate_option(user_option):
    """Evaluate the valid input from the user."""

    if user_option == 1:
        get_worldwide_stats(WORLDWIDE_URL)

    elif user_option == 2:
        print_list_to_user()

    elif user_option == 3:
        # Check if there are command line arguments
        country_input = input("Please enter a country name or two-letter"\
                           + " code of country to see COVID-19 stats.\n")
        print("\n")
        country = 'https://thevirustracker.com/free-api?countryTotal={}'\
            .format(get_country_code(country_input))
        get_country_stats(country)
    elif user_option == 4:
        prep_data()
    else:
        pass

def print_list_to_user():
        with open('countries-json/country-by-abbreviation.json') as json_file:
            number = 0
            string = ""
            for line in yaml.safe_load(json_file):
                string += "{}. {}:{}".format(number, line['COUNTRY'],\
                              line['ABBREVIATION'] + '\n')
                number += 1
        number = 0
        pager(string)

def check_country_is_valid(country):
    """Given the country full name or two-letter code; check if it's a valid
    country by searching the countries.txt file for a match.

    @param Country full name or country two-letter code.
    @return True if country is valid False otherwise.
    """

    l = []
    fhandler = open('countries.txt', 'r')
    for line in fhandler:
        temp = line.strip('\n').split(":")
        for e in temp:
            l.append(e)
    fhandler.close()
    if country.upper() in l:
        return True
    else:
        return False

def get_worldwide_stats(url):
    """Pull the world wide data from:
    https://thevirustracker.com/free-api?global=stats

    @param url of the worldwide stats
    """

    response = requests.get(url, headers={"User-Agent": "XY"})
    content = json.loads(response.content.decode())

    #TODO: format to f strings for cleaner look
    print()
    print("Total cases: {val:,}".format(val=content['results'][0]['total_cases']))
    print("Total New cases: {val:,}".format(val=content['results'][0]['total_new_cases_today']))
    print("Total Recovered cases: {val:,}".format(val=content['results'][0]['total_recovered']))
    print("Total Unresolved cases: {val:,}".format(val=content['results'][0]['total_unresolved']))
    print("Total Deaths: {val:,}".format(val=content['results'][0]['total_deaths']))
    print("Total Active Cases: {val:,}".format(val=content['results'][0]['total_active_cases']))
    print("Total Serious Cases: {val:,}".format(val=content['results'][0]['total_serious_cases']))

    death_rate = ((int(content['results'][0]['total_deaths'])) /\
          (int(content['results'][0]['total_cases']))) * 100
    print("Death Rate: {0:.2f}%".format(death_rate), '\n')

    if len(sys.argv) == 1:
        ask_user_if_continue()
    # We are on script mode. Exit.
    else:
        sys.exit()


def get_country_stats(data):
    """Pull the world wide data from:
    https://thevirustracker.com/free-api?global=stats
    https://thevirustracker.com/free-api?countryTotal={@param}

    @param url of the specific country stats
    """
    response = requests.get(data, headers={"User-Agent": "XY"})
    content = json.loads(response.content.decode())

    #TODO: format to f strings for cleaner look
    print('Country:', content['countrydata'][0]['info']['title'])
    print("Total Cases: {val:,}".format(val=content['countrydata'][0]['total_cases']))
    print('Total Active Cases: {val:,}'.format(val=content['countrydata'][0]['total_active_cases']))
    print('Total Cases Recovered: {val:,}'.format(val=content['countrydata'][0]['total_recovered']))
    print('Total Unresolved Cases: {val:,}'.format(val=content['countrydata'][0]['total_unresolved']))
    print('Total Deaths Reported: {val:,}'.format(val=content['countrydata'][0]['total_deaths']), '\n')

    death_rate = ((int(content['countrydata'][0]['total_deaths'])) /\
          (int(content['countrydata'][0]['total_cases']))) * 100
    print("Death Rate: {0:.2f}%".format(death_rate), '\n')

    if len(sys.argv) == 1:
        ask_user_if_continue()
    # We are on script mode. Exit.
    else:
        sys.exit(0)

def prep_data():
    '''Format the data for better visualization.

    Format: Date  Location   New Cases   New Deaths  Total Cases  Total Deaths
    '''
    amount_of_countries = int(input('How many countries would you like to'\
                                    + ' compare data? (15 countries max.) '))
    if amount_of_countries <= 1 or amount_of_countries > 15:
        # Default will be 10 if the number given as parameter is too high or
        # too low
        amount_of_countries = 10

    data = pd.read_csv('https://covid.ourworldindata.org/data/ecdc/full_data.csv')
    # Format the dates
    data['date'] = [dt.datetime.strptime(x, '%Y-%m-%d') for x in data['date']]

    # Format colum titles
    data.columns = ['Date', 'Country', 'New Cases', 'New Deaths', 'Total Cases',\
                    'Total Deaths']
    # Exclude countries from the data
    countries_to_exclude = ['World']
    data = data.loc[~(data['Country'].isin(countries_to_exclude))]
    # Group the data by Location and Date. Look only for Total Cases and
    data = pd.DataFrame(data.groupby(['Country', 'Date'])['Total Cases', \
                                        'Total Deaths'].sum()).reset_index()

    data = data.sort_values(by=['Country', 'Date'], ascending=False)
    filtered_data = data.drop_duplicates(subset=['Country'], keep='first')

    plot_data('Country', 'Total Cases', 'Total cases in the World',\
            filtered_data, size=amount_of_countries)


def plot_data(parameter, value, title, data, size):

    '''Plot cases and deaths as bar plot for X countries.
    Function to plot bar plots using Seaborn.

    '''
    pyplot.style.use('dark_background')
    f, ax = pyplot.subplots(1,1, figsize=(size*2, 5))
    data = data.sort_values([value], ascending=False).reset_index(drop=True)
    g = seaborn.barplot(data[parameter][0:size], data[value][0:size], palette='Set3')
    g.set_title('Number of {} - highest 10 values'.format(title))
    pyplot.show()

    if len(sys.argv) <= 1:
        print('\n')
        ask_user_if_continue()
    else:
        sys.exit()



def ask_user_if_continue():
    decision = input("Would you like to continue using COVID-19 Scrapper? (y/n)")
    if decision == 'y':
        print_menu()

    elif decision == 'n':
        print("Thank you for using COVID-19 Scrapper. Stay safe!")
        exit()


def get_country_code(country):
    """Retrieve the two-letter code from the .json file
    and return the code.
    """

    country_code = ""
    if check_country_is_valid(country):
        pass
    else:
        print("Please enter a valid country name or two-letter code.")
        print("Consult the available country list with -list")
        print('----------------------------------------------------------------------')
        sys.exit(1)

    with open('countries-json/country-by-abbreviation.json') as json_file:
        country  = country.upper()
        if len(country) > 2:
            for line in yaml.safe_load(json_file):
                if line['COUNTRY'] == country:
                    country_code = line['ABBREVIATION']
                    return country_code
        else:
            return country


if __name__ == "__main__":
    WORLDWIDE_URL = 'https://thevirustracker.com/free-api?global=stats'
    main()
