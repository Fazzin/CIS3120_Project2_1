'''
Main calls 7 functions
Step by Step Process
1) Prints introduction
2) Scrape imdb movie url into movie attribute variables
3) Use the variables to convert the data into the 1st dataframe using Pandas
4) Utilize one column, imdb ID, to make requests to OMDb API to recieve 6 new columns of information
5) Create the 2nd dataframe using the new data
6) Combine the 1st and 2nd dataframe 
7) Print the description statistics of the merged dataframe
8) Exports the merged dataframe into CSVs and SQLite (optional)

To run: python -m src.main 
''' 
from .introduction import introduction
from .scraping import scraping
from .dataframe import dataframe
from .dataframe_api import omdb_data
from .combined_dataframe import combining
from .to_csv import to_csv
from .to_sql import to_sql


def main():
    introduction()
    #Print statement before all the functions are applied
    print('''
    PRINTING MERGED DATAFRAME
    Please wait as this takes about 5-15 minutes depending on your machine!
    .......''')
    movies_url = {"https://www.imdb.com/chart/top/"}
    #Movie attributes from scraping into variables
    movie_title, movie_year, movie_time, movie_content_rating, movie_rating, imdb_id = scraping(movies_url)
    #Combine the attributes into a dataframe
    movie_dataframe = dataframe(movie_title, movie_year, movie_time, movie_content_rating, movie_rating, imdb_id)
    #Use OMDb API to add new columns and values into the dataframe
    dataframe_omdb = omdb_data(movie_dataframe)
    #Combines movie dataframe and the new dataframe with the API
    merged_dataframe = combining(movie_dataframe, dataframe_omdb)
    #Prints the merged dataframe 
    print(merged_dataframe)

    #OPTIONAL CSV export
    while(True):
        csv_export_answer = input("Would you like to export the merged dataframe as a CSV? [Y/N] ").strip().lower() #Ensures all answers will be in lower case
        if csv_export_answer in {"y", "yes"}:
            to_csv(merged_dataframe) #Converts merged dataframe into CSV
            break
        elif csv_export_answer in {"n", "no"}:
            print("Data will not be exported.")
            break
        print("Please enter y / yes or n / no")

    #OPTIONAL SQL export
    while(True):
        sql_export_answer = input("Would you like to export the merged dataframe into a SQL database? [Y/N] ").strip().lower() #Ensures all answers will be in lower case
        if sql_export_answer in {"y", "yes"}:
            to_sql(merged_dataframe) #Converts merged dataframe into SQL
            break
        elif sql_export_answer in {"n", "no"}:
            print("Data will not be exported.")
            break
        print("Please enter y / yes or n / no")

    print(f'Printing the merged dataframe statistics \n{merged_dataframe.describe()}') #Includes only numeric data

if __name__ == "__main__":
    main()