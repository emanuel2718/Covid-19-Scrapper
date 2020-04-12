# Covid-19-Scrapper [![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/DAVFoundation/captain-n3m0/blob/master/LICENSE)


This started as a simple command line interface web scrapper script for COVID-19 data.
This was done as a way for me to practice Python programming language and at the same time
gather important data for me and whoever want to use this script.
All the COVID-19 data is scraped using https://virustracker.com free API.
Sources used: WHO, CDC, ECDC, NHC, DXY

For the original source of the data please visit: [World Health Organization website](https://www.who.int)

**WARNING:** As of 04/12/2020 this is not providing accurate data for some
countries (i.e Puerto Rico). But countries like USA are still begin updated
correctly; source is no longer updating the data.
	
	
# Usage:

Clone this repo:
```sh
git clone https://github.com/emanuel2718/Covid-19-Scrapper.git
```
Intall requirements:
```sh
pip install -r requirements.txt
```

There are two main ways to get the data:
1. Run the program with: ```python covid19.py```
2. Or type optional arguments:

	1. To get worldwide data only: ```python -w```
	
	2. To get list of countries and two-letter country codes available: ```python covid19.py -list```
	
	3. To get data for a specific country: ```python covid19.py -s <country>``` (Country can be two-letter country code)
	
	4. To visualize the data in a plot graph: ```python covid19.py -g```
	
	4. To get help: ```python -h``` or ```python --help```
	

	
## Screenshots of the non-script mode:

#### Output 1:

<img width="717" alt="worldwide_data_output" src="https://user-images.githubusercontent.com/55965894/76808630-b79a2080-67be-11ea-809c-a61b61a42562.png">

#### Output 2:

	By selecting option 2; a pager page, containing all the countries and their 
	respective abbreviations, will appear on the screen. To quit just press 'q'.

#### Output 3 (Country-specific Data):
<img width="725" alt="country_data_output" src="https://user-images.githubusercontent.com/55965894/76808635-b963e400-67be-11ea-9bad-2388ccd2ec05.png">

#### Output 4:
<img width="995" alt="Pasted Graphic" src="https://user-images.githubusercontent.com/55965894/77498256-94f2b200-6e25-11ea-8990-a5b7aed34cc7.png">




## Future Implementations:

- [x] Add more data alternatives (i.e Death Rates, % of Populations, etc.)
- [x] Make it interactive (Add main menu for alternatives)
- [x] Add data visualization (Graphs, plots, etc.)
- [ ] Display changes for the day in data (i.e +- X amount of cases today)
- [ ] Make a GUI
- [ ] Make a webpage


