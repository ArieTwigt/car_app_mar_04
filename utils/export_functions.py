import pandas as pd
import os


def export_df_to_csv(df: pd.DataFrame,
                     brand_name: str="export") -> None:
    '''
    
    Exports a pandas DataFrame to csv

    Input:

    * df: The pandas DataFrame to export.
    * brand_name: (optional) name for the folder.

    '''


    # export_folder_name
    export_folder_name = 'data'

    # define the folder path
    folder_path = f"{export_folder_name}/{brand_name}"

    # create the folder and subfolders
    os.makedirs(folder_path, exist_ok=True)

    # define the file path
    file_path = f"{folder_path}/export_{brand_name}.csv"    

    # export the DataFrame
    df.to_csv(file_path)

   