'''
Creates a dataframe using the scraped data of movie attributes
Parameters are lists that include str, int, and float
Returns dataframe 
'''

import pandas as pd

def dataframe(title, year, time, content_rating, rating, id):
    data = {
        'Title' : title,
        'Year' : year,
        'RunTime' : time,
        'ContentRating' : content_rating,
        'Rating' : rating,
        'Imdb_Id' : id
    }
    df = pd.DataFrame(data) #Converts data into a dataframe
    return df
