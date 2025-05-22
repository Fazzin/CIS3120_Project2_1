'''
The function converts a dataframe into a csv file
It only has one parameter, dataframe
Prints how many rows saved to the dataframe 
'''

def to_csv(dataframe):
    dataframe.to_csv('Merged_Movie_Dataframe.csv', index=False) #COnverts dataframe into csv and remove indexing
    print(f'{len(dataframe)} rows saved to Merged_Movie_Dataframe.csv') #Print how many rows of data has been saved to the csv file
