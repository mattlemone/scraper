import csv
import requests
from tqdm import tqdm

# Sample cities
cities = ['New York,NY', 'Los Angeles,CA', 'Chicago,IL', 'Lehi,UT', 'Logan,UT']

def get_city_government_info(city):
    city_name, state = city.split(",")
    state = state.strip()
    
    try:
        # Example OCDS API endpoint (this may vary based on actual OCDS data sources)
        api_url = f'https://example-ocds-api.com/entities?q={city_name}&state={state}'
        
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            
            # Extracting relevant information (example, actual implementation will vary)
            if data and 'entities' in data:
                entity = data['entities'][0]  # Assuming the first entity is the relevant one
                return {
                    'city': city_name,
                    'state': state,
                    'name': entity.get('name'),
                    'address': entity.get('address'),
                    'phone_number': entity.get('phone_number'),
                    'website': entity.get('website'),
                    'county': entity.get('county'),
                }
            else:
                return {
                    'city': city_name,
                    'state': state,
                    'name': None,
                    'address': None,
                    'phone_number': None,
                    'website': None,
                    'county': None,
                }
        else:
            print(f'Failed to fetch data for {city}. Status code: {response.status_code}')
            return {
                'city': city_name,
                'state': state,
                'name': None,
                'address': None,
                'phone_number': None,
                'website': None,
                'county': None,
            }
    except Exception as e:
        print(f'Error fetching data for {city}: {e}')
        return {
            'city': city_name,
            'state': state,
            'name': None,
            'address': None,
            'phone_number': None,
            'website': None,
            'county': None,
        }

# Main script
if __name__ == "__main__":
    city_government_infos = []

    for city in tqdm(cities, desc='Processing Cities'):
        info = get_city_government_info(city)
        city_government_infos.append(info)
        # Add time delay if necessary to avoid rate limits
        
    # Define CSV file path
    csv_file = "city_government_info.csv"

    # Define CSV fieldnames based on the keys of the dictionaries
    fieldnames = ['city', 'state', 'name', 'address', 'phone_number', 'website', 'county']

    # Writing data to CSV
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write header
        writer.writeheader()

        # Write rows
        writer.writerows(city_government_infos)

    print(f"Data has been exported to {csv_file}")
