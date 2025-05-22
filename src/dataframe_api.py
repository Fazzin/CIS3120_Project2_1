'''
This function pulls data from the OMDb API server using the IMDb id column from the dataframe
There is only one parametr which is the dataframe 
Returns a new dataframe
'''

import requests
import os
import time
import pandas as pd
from dotenv import load_dotenv

#Loads environment variables from .env file (To hide API key)
load_dotenv()
API_KEY = os.getenv("OMDB_API_KEY")

def omdb_data(df):
    omdb_results = []
    empty_data = []
    for id in df['Imdb_Id']:
        try:
            #Using IMDb id and the api key to pull from the api server
            url = f'http://www.omdbapi.com/?i={id}&apikey={API_KEY}' 
            page = requests.get(url)
            data = page.json()
            #Check if the API response was successful (movie data was found)
            if data.get('Response') == 'True':
                omdb_results.append({'Language': data.get('Language'), 
                                     'Metascore': data.get('Metascore'), 
                                     'Country': data.get('Country'), 
                                     'BoxOffice': data.get('BoxOffice'), 
                                     'Director': data.get('Director'), 
                                     'Awards': data.get('Awards')
                                    })
            else: #If movie isn't found then it is left empty
                for key in ['Language', 'Metascore', 'Country', 'BoxOffice', 'Director', 'Awards']:
                    empty_data[key] = None
                    omdb_results.append(empty_data)
            time.sleep(0.5) #Pauses the program for 0.5 seconds. Prohibits program from overwhelming the api server

        except Exception: #Append empty values if there is an exception
            print(f'Error fetching {id}: {Exception}')
            for key in ['Language', 'Metascore', 'Country', 'BoxOffice', 'Director', 'Awards']:
                    empty_data[key] = None
                    omdb_results.append(empty_data)

    #Converts data into dataframe               
    omdbDataFrame = pd.DataFrame(omdb_results)
    return omdbDataFrame
