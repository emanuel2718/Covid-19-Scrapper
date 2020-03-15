import requests
import json
import yaml

# Simple web scraping script to get covid-19 data using https://thevirustracker.com free API.
# Created by Emanuel Ramirez on March 15, 2020



def get_country_code():
    country_code = ""
    user_input = input("Please enter a country name or two-letter code of country to see COVID-19 stats: ")
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


data = 'https://thevirustracker.com/free-api?countryTotal={}'.format(get_country_code())
#url = 'https://thevirustracker.com/free-api?global=stats'

response = requests.get(data)
content = json.loads(response.content.decode())

print('Country:', content['countrydata'][0]['info']['title'])
print('Total Cases:', content['countrydata'][0]['total_cases'])
print('Total Active Cases:', content['countrydata'][0]['total_active_cases'])
print('Total Cases Recovered:', content['countrydata'][0]['total_recovered'])
print('Total Unresolved Cases:', content['countrydata'][0]['total_unresolved'])
print('Total New Cases Today:', content['countrydata'][0]['total_active_cases'])
print('Total Deaths Reported:', content['countrydata'][0]['total_deaths'], "\n")
#print('Death Rate in Puerto Rico', (int(content['countrydata'][0]['total_deaths']) /\
      #int(content['countrydata'][1]['total_cases'])))

