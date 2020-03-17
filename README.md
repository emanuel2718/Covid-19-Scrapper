# Covid-19-Scrapper

This started as a simple command line interface web scrapper script for COVID-19 data.
This was done as a way for me to practice Python programming language and at the same time
gather important data for me and whoever want to use this script.
All the COVID-19 data is scraped using https://virustracker.com free API.
Sources used: WHO, CDC, ECDC, NHC, DXY
	
For the original source of the data please visit: [World Health Organization website](https://www.who.int)
	
## How to use:
You can see worldwide data by just pressing '1'. This will display COVID-19 data for the whole world.
You can see the available country options and their respective two-letter code abbreviations by typing '2'.
To see specific countries data: Press '3' and either type the country name or two-letter code for the respective country.
Input checking is case insensitive.

## Output 1 (Worldwide Data):

<img width="717" alt="worldwide_data_output" src="https://user-images.githubusercontent.com/55965894/76808630-b79a2080-67be-11ea-809c-a61b61a42562.png">

## Output 2:

By selecting option 2; a pager page, containing all the countries and their 
respective abbreviations, will appear on the screen. To quit just press 'q'.

## Output 3 (Country-specific Data):
<img width="725" alt="country_data_output" src="https://user-images.githubusercontent.com/55965894/76808635-b963e400-67be-11ea-9bad-2388ccd2ec05.png">


## Future Implementations:

- [x] Add more data alternatives (i.e Death Rates, % of Populations, etc.)
- [x] Make it interactive (Add main menu for alternatives)
- [ ] Display changes for the day in data (i.e +- X amount of cases today)
- [ ] Make a GUI
- [ ] Make a webpage
