import requests
from typing import List, Dict


def import_cars_by_brand(brand: str) -> List[Dict]:
    '''
    
    Function to import data from the RDW, given a brand name.

    Params:
    * brand: The brand you would like to import
    
    '''
    # uppercase the brand
    brand_upper = brand.upper().strip()

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute request
    response = requests.get(endpoint)

    # extract the data from the response
    data = response.json()

    # check if the list is not empty
    if len(data) == 0:
        raise ValueError(f"No cars found for {brand}")

    return data