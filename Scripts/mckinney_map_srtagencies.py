import os
import gql
from gql.transport.aiohttp import AIOHTTPTransport
import pandas as pd
from rental_middleware import getUrl,generateToken

def get_location_mappings():
    """Fetch all location mappings with pagination and lowercase normalization"""
    token = generateToken()
    service_url = getUrl()
    transport = AIOHTTPTransport(url=service_url, headers={"Authorization": f"Bearer {token}"})
    client  = gql.Client(transport=transport, fetch_schema_from_transport=True)
    
    
    all_data = []
    limit = 10000
    offset = 0
    total = None
    
    try:
        while True:
            result = client.execute(gql.gql('''
                query Data($limit: Int!, $offset: Int!) {
                    getLocationMapping(limit: $limit, offset: $offset) {
                        data {
                            name
                            agency { agency_name }
                        }
                        count
                    }
                }
            '''), variable_values={"limit": limit, "offset": offset})
            
            data_chunk = result['getLocationMapping']['data']
            all_data.extend(data_chunk)
            
            if total is None:
                total = result['getLocationMapping']['count']
            
            if (offset := offset + limit) >= total:
                break
                
    except Exception as e:
        print(f"Failed to fetch location mappings: {str(e)}")
        raise

    return {
        item['name'].strip().lower(): item['agency']['agency_name'].strip()
        for item in all_data
        if item.get('name') and item.get('agency', {}).get('agency_name')
    }

def process_excel_files(input_folder="SRTS_OUTPUT"):
    """Process and overwrite Excel files in the input folder"""
    os.makedirs(input_folder, exist_ok=True)
    location_map = get_location_mappings()
    
    processed = 0
    skipped = []
    
    for filename in os.listdir(input_folder):
        if not filename.endswith(".xlsx"):
            continue
            
        file_path = os.path.join(input_folder, filename)
        
        try:
            df = pd.read_excel(file_path)
            
            if 'EXIT LANE/LOCATION' not in df.columns:
                skipped.append(filename)
                continue
            df['TOLL AGENCY'] = (
                df['EXIT LANE/LOCATION']
                .astype(str)
                .str.strip()
                .str.lower()
                .map(location_map)
                .fillna("MCKINNEY")
            )
            
            df.to_excel(file_path, index=False)
            processed += 1
            
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")
            skipped.append(filename)
    
    print(f"\nProcessing complete:")
    print(f"- Updated files: {processed}")
    print(f"- Skipped files: {len(skipped)}")
    if skipped:
        print("Skipped files list:\n" + "\n".join(f"  - {f}" for f in skipped))

if __name__ == "__main__":
    process_excel_files()