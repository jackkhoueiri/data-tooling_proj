from geopy.geocoders import Nominatim
import pandas as pd
import time

# Initialize the Nominatim geocoder
geolocator = Nominatim(user_agent="restaurant_mapper")

# Load your dataset with restaurant addresses
data = pd.read_csv('data/top_restaurants_paris.csv')  # Replace with your dataset

# Function to geocode an address and get latitude and longitude
def get_lat_lon(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            print(f"Address not found: {address}")
            return None, None
    except Exception as e:
        print(f"Error for {address}: {e}")
        return None, None

# Loop through your dataset and geocode each address
latitude = []
longitude = []

for index, row in data.iterrows():
    address = row['address']  # from address col in CSV
    lat, lon = get_lat_lon(address)
    latitude.append(lat)
    longitude.append(lon)
    time.sleep(2)

# Add latitude and longitude columns to your dataset
data['latitude'] = latitude
data['longitude'] = longitude

# Save the updated dataset with coordinates
data.to_csv('restaurants_with_coordinates.csv', index=False)
