import pandas as pd
import requests
import time

# Load city data from CSV file
city_data = pd.read_csv('worldcities.csv')

# Define function to fetch weather data for a city from API
def fetch_weather_data(city):
    api_key = '2f5bebb7c5ec8da6c4926b7f4f78aa47'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
# Fetch weather data for each city and store in a list
weather_data_list = []
for city in city_data['city']:
    print(f"Fetching weather data for {city}...")
    try:
        weather_data = fetch_weather_data(city)
        if weather_data:
            weather_data_list.append({
                'city': city,
                'Temperature (C)': weather_data['main']['temp'],
                'Weather': weather_data['weather'][0]['description']
            })
            print(f"Successfully fetched weather data for {city}")
        else:
            print(f"No weather data available for {city}")
    except Exception as e:
        print(f"Error fetching weather data for {city}: {e}")

    # Introduce a 1-second delay between requests
    time.sleep(2)

# Create DataFrame from weather data list
weather_df = pd.DataFrame(weather_data_list)

# Merge city data with weather data
integrated_data = pd.merge(city_data, weather_df, on='city', how='inner')

# Save integrated data to CSV file
integrated_data.to_csv('integrated_weather_data.csv', index=False)