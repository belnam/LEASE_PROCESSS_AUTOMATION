import pandas as pd
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

def reference_equipmentID(equipment_id):
    url = "https://amazon.backend.innovativetoll.com/check-asset-exists"
    payload = {"equipment_id": str(equipment_id)}

    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Failed to fetch data for equipment_id {equipment_id}. Status code: {response.status_code}")

def processrentals():
    rawfiles_dir = "SRTS_OUTPUT/scan_705_amazon_xtra_rental_tolls_05-15-2025_(bot)_1747371998.xlsx"
    rawfiles_df = pd.read_excel(rawfiles_dir, dtype=str)
    
    # Get unique equipment IDs
    unique_equipment_ids = rawfiles_df['EQUIPMENT ID'].unique()
    
    # Dictionary to cache API responses to avoid redundant API calls for the same EQUIPMENT ID
    api_cache = {}

    start = time.time()

    # Function to fetch data for a single equipment ID
    def fetch_data(equipment_id):
        if equipment_id not in api_cache:
            api_data = reference_equipmentID(equipment_id)
            api_cache[equipment_id] = api_data
        return equipment_id

    # Use ThreadPoolExecutor to fetch data concurrently
    with ThreadPoolExecutor(max_workers=200) as executor:
        futures = [executor.submit(fetch_data, equipment_id) for equipment_id in unique_equipment_ids]
        
        for future in as_completed(futures):
            equipment_id = future.result()
            api_data = api_cache[equipment_id]
            
            if api_data["data"]["exists"]:
                if api_data["data"]["inCurrentAAP"] is True:
                    license_plate = api_data["data"]["data"]["license_plate"]
                    license_plate_state = api_data["data"]["data"]["license_plate_state"]
                elif api_data["data"]["inCurrentAAP"] is False:
                    license_plate = api_data["data"]["searchedAsset"]["license_plate"]
                    license_plate_state = api_data["data"]["searchedAsset"]["license_plate_state"]
                
                # Update all rows with the same equipment ID
                mask = rawfiles_df['EQUIPMENT ID'] == equipment_id
                rawfiles_df.loc[mask, 'LP'] = license_plate
                rawfiles_df.loc[mask, 'LP STATE'] = license_plate_state

    rawfiles_df.to_excel(rawfiles_dir, index=False)
    stop = time.time()
    print(f'Done processing in {stop - start} seconds')

if __name__ == '__main__':
    processrentals()