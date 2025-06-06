'''
This function combines two dataframes into one
Parameters are dataframe1 and dataframe2
Returns the merged dataframe. 
'''
import pandas as pd

def combining(df1, df2):
    #Concat stacks dataframe1 and dataframe2. Appends columns/rows from one dataframe to another
    #Resets the index to 0 to ensure consistency and combines columns side-by-side
    merged_dataframe = pd.concat([df1.reset_index(drop=True), df2.reset_index(drop=True)], axis = 1)
    return merged_dataframe
