import pandas as pd
import requests
from sqlalchemy import create_engine

# Your OpenWeatherMap API key
api_key = "2f5bebb7c5ec8da6c4926b7f4f78aa47"

# Define the base URL
base_url = "http://api.openweathermap.org/data/2.5/weather"

def extract_data():
    # Extract data from a CSV file
    csv_url = 'cities.csv'
    data_csv = pd.read_csv(csv_url)
    return data_csv

def fetch_weather_data(city, country):
    api_url = f"{base_url}?q={city},{country}&appid={api_key}&units=metric"
    response = requests.get(api_url)
    response.raise_for_status()  # If the response was successful, no Exception will be raised
    return response.json()

def transform_data(data_csv):
    weather_data = []
    for index, row in data_csv.iterrows():
        city = row['city']
        country = row['country']
        try:
            data_api = fetch_weather_data(city, country)
            weather_info = {
                "city": city,
                "country": country,
                "temperature": data_api["main"]["temp"],
                "weather": data_api["weather"][0]["description"],
                "humidity": data_api["main"]["humidity"],
                "pressure": data_api["main"]["pressure"],
                "wind_speed": data_api["wind"]["speed"]
            }
            weather_data.append(weather_info)
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data for {city}, {country}: {e}")
    
    weather_df = pd.DataFrame(weather_data)
    return weather_df

def load_data(weather_df):
    # Database connection string
    db_connection_string = 'postgresql+psycopg2://username:password@localhost:5432/mydatabase'
    
    # Create a database engine
    engine = create_engine(db_connection_string)
    
    # Load data into the database
    weather_df.to_sql('cleaned_weather_data', engine, if_exists='replace', index=False)
    print(f"Weather data successfully fetched and saved to the database.")

def main():
    # Extract
    data_csv = extract_data()
    
    # Transform
    weather_df = transform_data(data_csv)

    print(weather_df)
    
    # Load
    load_data(weather_df)

if __name__ == '__main__':
    main()
