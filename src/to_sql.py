'''
This function converts a dataframe to a sql database by creating a database using sqlite
It iterates through the parameter, dictionaries, to convert every dataframe into a table in the database.
The function prints the table name, and how many rows were saved to the database name.
'''
import sqlite3

def to_sql(dataframe, db_file="Merged_Movie_Dataframe.db", table_name = 'Movies'):
    db_conn = sqlite3.connect('Merged_Movie_Dataframe.db') #Creates database 
    #Converts dataframe into a SQL database. The table are used as names.
    dataframe.to_sql(table_name, db_conn, if_exists="replace", index=False) #If data exists, the data is replaced with the new one. Also removes index.
    print(f'{len(dataframe)} rows saved to {db_file}')
    db_conn.close()
