import pandas as pd
from typing import List

def convert_list_to_df(items_list: List) -> pd.DataFrame:
    '''
    
    Function to convert a list to a pandas DataFrame:

    Inputs:
    * items_list: List with items to convert

    '''
    # convert the list to a pandas DataFrame
    items_df = pd.DataFrame(items_list)

    return items_df