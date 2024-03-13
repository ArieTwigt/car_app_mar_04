from utils.import_functions import import_cars_by_brand
from utils.conversion_functions import convert_list_to_df
from utils.export_functions import export_df_to_csv

from tqdm import tqdm

# input the brand
selected_brands_list = input("Choose a brand:\n").split(" ")

# loop trough the brands
for selected_brand in tqdm(selected_brands_list):

    try:
        # import the cars
        cars_list = import_cars_by_brand(selected_brand)
    except ValueError:
        print(f"Skipping {selected_brand}")
        continue

    # convert the list of cars to a pandas DataFrame
    cars_df = convert_list_to_df(cars_list)

    # export the DataFrame to csv
    export_df_to_csv(cars_df, selected_brand)



