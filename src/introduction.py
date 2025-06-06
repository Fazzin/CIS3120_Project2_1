'''
Prints the introduction
No parameters
'''

def introduction():
    print('''
        This project scrapes IMDb's Top 250 movie data using embedded JSON to extract the movie title, year, runtime, content rating and rating.
        There will be 3 dataframes in total.
        The 1st dataframe is the regular data. The 2nd dataframe stores data from a movie API. The 3rd dataframe combines the 1st and 2nd dataframe.
        Dataframe 3 will also contain the decscription statistics.
        Finally the data will be exported to a csv file and sql database.
          ''')
