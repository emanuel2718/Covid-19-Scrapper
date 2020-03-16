#!/usr/bin/python
from pydoc import pager
from time import sleep
#import locale
import requests
import json
import yaml

# Simple web scraping script to get covid-19 data using https://thevirustracker.com free API.
# Created by Emanuel Ramirez on March 15, 2020


def main():
    done = False
    while not done:
        print_menu()
        user_input = input("Please, enter option: ")
        print('------------------------------------------------')
        option_info = check_validity(user_input)
        if option_info != -1:
            pass
            if option_info == 4:
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
    print()
    print("COVID-19 Stats Scrapper. Please, select a number." + "\n")
    print("1. To see worldwide stats.")
    print("2. To see a list of the available countries and their"\
          + " respective abbreviations.")

    print("3. To type a country or abrreviation and see their stats.")
    print("4. Exit")



def check_validity(option):
    if option.isdigit():
        numeric_option = int(option)
        if numeric_option >=1 and numeric_option <= 4:
            return numeric_option
        else:
            return -1
    else:
        return -1


def evaluate_option(user_option):
    if user_option == 1:
        worldwide_url = 'https://thevirustracker.com/free-api?global=stats'
        get_worldwide_stats(worldwide_url)

    elif user_option == 2:
        with open('countries-json/country-by-abbreviation.json') as json_file:
            number = 0
            string = ""
            for line in yaml.safe_load(json_file):
                string += "{}. {}:{}".format(number, line['COUNTRY'],\
                              line['ABBREVIATION'] + '\n')
                number += 1
        number = 0
        pager(string)

    elif user_option == 3:
        country = 'https://thevirustracker.com/free-api?countryTotal={}'.format(get_country_code())
        get_country_stats(country)

    else:
        pass


def get_worldwide_stats(url):
    # Check locale for output formatting?
    response = requests.get(url)
    content = json.loads(response.content.decode())

    total_cases = content['results'][0]['total_cases']
    new_cases = content['results'][0]['total_new_cases_today']
    recovered = content['results'][0]['total_recovered']
    unresolved = content['results'][0]['total_unresolved']
    total_deaths = content['results'][0]['total_deaths']
    total_new_deaths = content['results'][0]['total_new_deaths_today']
    total_active = content['results'][0]['total_active_cases']
    total_serious = content['results'][0]['total_serious_cases']

    death_rate = ((int(total_deaths)) / (int(total_cases))) * 100

    print()
    print("Total cases: {val:,}".format(val=total_cases))
    print("Total New cases: {val:,}".format(val=new_cases))
    print("Total Recovered cases: {val:,}".format(val=recovered))
    print("Total Unresolved cases: {val:,}".format(val=unresolved))
    print("Total Unresolved cases: {val:,}".format(val=unresolved))
    print("Total Deaths: {val:,}".format(val=total_deaths))
    print("Total New Deaths: {val:,}".format(val=total_new_deaths))
    print("Total Active cases: {val:,}".format(val=total_active))
    print("Total Serious cases: {val:,}".format(val=total_serious), '\n')
    print("Death Rate: {0:.2f}%".format(death_rate), '\n')
    ask_user_if_continue()


def get_country_stats(data):
    #TODO: Decide which looks cleaner betwen worlwide or counrty functions
    response = requests.get(data)
    content = json.loads(response.content.decode())


    print('Country:', content['countrydata'][0]['info']['title'])
    print("Total Cases: {val:,}".format(val=content['countrydata'][0]['total_cases']))
    print('Total Active Cases: {val:,}'.format(val=content['countrydata'][0]['total_active_cases']))
    print('Total Cases Recovered: {val:,}'.format(val=content['countrydata'][0]['total_recovered']))
    print('Total Unresolved Cases: {val:,}'.format(val=content['countrydata'][0]['total_unresolved']))
    print('Total New Cases Today: {val:,}'.format(val=content['countrydata'][0]['total_active_cases']))
    print('Total Deaths Reported: {val:,}'.format(val=content['countrydata'][0]['total_deaths']), '\n')
    death_rate = ((int(content['countrydata'][0]['total_deaths'])) /\
          (int(content['countrydata'][0]['total_cases']))) * 100
    print("Death Rate: {0:.2f}%".format(death_rate), '\n')
    ask_user_if_continue()


def ask_user_if_continue():
    decision = input("Would you like to continue using COVID-19 Scrapper? (y/n)")
    if decision == 'y':
        # Maybe use clear here?
        print_menu()
    elif decision == 'n':
        print("Thank you for using COVID-19 Scrapper. Stay safe!")
        exit()


def get_country_code():
    country_code = ""
    user_input = input("Please enter a country name or two-letter code "\
                       + "of country to see COVID-19 stats.\n")
    print("\n")
    with open('countries-json/country-by-abbreviation.json') as json_file:
        # Format the input
        # TODO: need to check if country is not in database
        user_input  = user_input.upper()
        if len(user_input) > 2:
            for line in yaml.safe_load(json_file):
                if line['COUNTRY'] == user_input:
                    country_code = line['ABBREVIATION']
                    return country_code
        else:
            #coutry_code = user_input
            return user_input


if __name__ == "__main__":
    main()
