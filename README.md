# CIS3120_Project2_2 
CIS 3120 Programming to Analytics Project 2 Question 1
### Requires 
·[Python](https://www.python.org/downloads/) 
·[Requests](https://pypi.org/project/requests/)
·[BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
·[Pandas](https://pypi.org/project/pandas/)
·[python-dotenv](https://pypi.org/project/python-dotenv/)

## What does this repository do?

| 1 | **Scrape** data from IMDb's Top 250 chart  
| 2 | **Convert** the data into Dataframe using pandas ('Title', 'Year', 'Runtime', 'Content Rating', 'Ratings', 'IMDb IDs')  
| 3 | **Utilize** OMDb API and **Extract** the data using IMDb IDs as the column  
| 4 | **Converts** the data into the second dataframe ('Language', 'Metascore', 'Country', 'Box Office', 'Director', 'Awards')  
| 5 | **Exports** and stores the data into **CSVs** and a single **SQLite Database** (OPTIONAL)  

## How do I run this repository?
| 1 | Clone the repo  
| 2 | Change directory to project root  
| 3 | Ensure the requirements are fufilled: · Python · Requests · BeautifulSoup4 · Pandas · Matplotlib · python-dotenv  
| 3 | Run main file.  **Note: The runtime is about 5-15 minutes, depending on your machine**  
        · python -m src.main
