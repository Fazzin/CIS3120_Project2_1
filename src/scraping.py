'''
Scrapes movie data from IMDb Top 100 (or similar) chart pages using embedded JSON scripts.
Parameter requires url(s)
Scrapes from two different JSON scripts
Returns a list of movie: titles, years, runtime, content rating, and review rating
'''

import requests
from bs4 import BeautifulSoup
import json

def scraping(urls):
    #Initalized lists to store data
    movie_titles = []
    movie_years = []
    movie_duration = []
    movie_content_ratings = []
    movie_ratings = []
    movie_ids = []
    headers = {
        #Websites that block us so this user-agent header ensures the website knows we're a "browser"
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    #Iterate through each url (if there are multiple urls)
    for url in urls:
        page = requests.get(url, headers=headers)
        #Handle failed requests
        if page.status_code != 200:
            print(f'Failed to send a GET request to {url} because the status_code = {page.status_code}')
            continue
        
        soup = BeautifulSoup(page.content, 'html.parser')
        data1 = json.loads(soup.find('script', {'type': 'application/ld+json'}).text) #json script 1 .text to convert to string
        data2 = soup.find('script', {'type': 'application/json'}) #json script 2
        data2_string = json.loads(data2.string) #.string to convert to string

        json_script_data1 = data1['itemListElement'] #JSON Script 1: Get list of movies (title, duration, content rating)
        json_script_data2 = data2_string['props']['pageProps']['pageData']['chartTitles']['edges'] #JSON Script 2: Get list of movies (year, IMDb rating)
        
        #Iterate through JSON Script 1
        for item in json_script_data1:
            movie_title = item['item']['name']
            movie_run_time = item['item']['duration'].replace('PT', "") #Replaces PT with "" (Removes it) Runtime in hr/min
            movie_content_rating = item['item'].get('contentRating', None) #PG, R, etc.. may not exist
            
            #Appending title, run_time, content_rating
            movie_titles.append(movie_title)
            movie_duration.append(movie_run_time)
            movie_content_ratings.append(movie_content_rating)

        #Iterate through JSON Script 1
        for node in json_script_data2:
            item2 = node['node'] #Node contains the actual data
            movie_year = item2['releaseYear']['year']
            movie_rating = item2['ratingsSummary']['aggregateRating']
            movie_id = item2['id']

            #Appending year, rating
            movie_years.append(movie_year)
            movie_ratings.append(movie_rating)
            movie_ids.append(movie_id)

    return movie_titles, movie_years, movie_duration, movie_content_ratings, movie_ratings, movie_ids
