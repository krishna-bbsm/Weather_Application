import requests
import click
import json
import time

# Replace with your WeatherAPI key
API_KEY = 'dce8dace1ace4b7fb2b132613230510'

# API URL
BASE_URL = 'https://api.weatherapi.com/v1/'

# Function to fetch current weather by city name
def get_current_weather(city_name):
    """
    Get current weather for a given city.
    
    Args:
        city_name (str): The name of the city.
        
    Returns:
        dict: Weather data for the city.
    """
    try:
        # Build the URL for the current weather API request
        url = f'{BASE_URL}current.json?key={API_KEY}&q={city_name}'
        
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check for HTTP status errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {str(e)}")
        return None

# Function to fetch 14-day weather forecast by city name
def get_14_day_forecast(city_name):
    """
    Get a 14-day weather forecast for a given city.
    
    Args:
        city_name (str): The name of the city.
        
    Returns:
        dict: Weather forecast data for the city.
    """
    try:
        # Build the URL for the 14-day forecast API request
        url = f'{BASE_URL}forecast.json?key={API_KEY}&q={city_name}&days=14'
        
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check for HTTP status errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather forecast data: {str(e)}")
        return None

# Function to fetch historical weather data for a specific date and city
def get_historical_weather(city_name, date):
    """
    Get historical weather data for a specific date and city.
    
    Args:
        city_name (str): The name of the city.
        date (str): The date in YYYY-MM-DD format.
        
    Returns:
        dict: Historical weather data for the city on the specified date.
    """
    try:
        # Build the URL for the historical weather API request
        url = f'{BASE_URL}history.json?key={API_KEY}&q={city_name}&dt={date}'
        
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check for HTTP status errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical weather data: {str(e)}")
        return None

# Function to fetch astronomy data for a given location
def get_astronomy_data(city_name):
    """
    Get astronomy data for a given location.
    
    Args:
        city_name (str): The name of the city.
        
    Returns:
        dict: Astronomy data for the city.
    """
    try:
        # Build the URL for the astronomy API request
        url = f'{BASE_URL}astronomy.json?key={API_KEY}&q={city_name}'
        
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check for HTTP status errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching astronomy data: {str(e)}")
        return None

# Function to fetch air quality data for a given location
def get_air_quality_data(city_name):
    """
    Get air quality data for a given location.
    
    Args:
        city_name (str): The name of the city.
        
    Returns:
        dict: Air quality data for the city.
    """
    try:
        # Build the URL for the air quality API request
        url = f'{BASE_URL}current.json?key={API_KEY}&q={city_name}'
        
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check for HTTP status errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Extract and return the air quality data
        return data.get('air_quality')
    except requests.exceptions.RequestException as e:
        print(f"Error fetching air quality data: {str(e)}")
        return None

# Function to save favorites to a JSON file
def save_to_file(filename, favorite_cities):
    """
    Save favorite cities to a JSON file.
    
    Args:
        filename (str): The name of the JSON file.
        favorite_cities (list): List of favorite city names.
    """
    with open(filename, 'w') as file:
        json.dump(favorite_cities, file)

# Function to load favorites from a JSON file
def load_from_file(filename):
    """
    Load favorite cities from a JSON file.
    
    Args:
        filename (str): The name of the JSON file.
        
    Returns:
        list: List of favorite city names.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to add a city to the favorite list
def add_favorite(city_name, favorite_cities):
    """
    Add a city to the list of favorite cities if it's not already present.
    
    Args:
        city_name (str): The name of the city to add.
        favorite_cities (list): List of favorite city names.
        
    Returns:
        list: Updated list of favorite city names.
        bool: True if the city was added, False if it was already in the list.
    """
    if city_name not in favorite_cities:
        favorite_cities.append(city_name)
        return favorite_cities, True
    else:
        return favorite_cities, False

# Function to remove a city from the favorite list
def remove_favorite(city_name, favorite_cities):
    """
    Remove a city from the list of favorite cities.
    
    Args:
        city_name (str): The name of the city to remove.
        favorite_cities (list): List of favorite city names.
        
    Returns:
        list: Updated list of favorite city names.
    """
    if city_name in favorite_cities:
        favorite_cities.remove(city_name)
    return favorite_cities

# Function to list favorite cities and display their current weather
def list_favorites(favorite_cities):
    """
    List favorite cities and display their current weather.
    
    Args:
        favorite_cities (list): List of favorite city names.
    """
    if favorite_cities:
        print("Favorite Cities:")
        for city in favorite_cities:
            weather_data = get_current_weather(city)
            if weather_data:
                print(f"{city}:")
                display_weather(weather_data)
    else:
        print("No favorite cities yet.")

# Function to search for a city and provide autocomplete suggestions
def search_city(query):
    """
    Search for a city and provide autocomplete suggestions.
    
    Args:
        query (str): The search query.
        
    Returns:
        dict: Search results.
    """
    try:
        # Build the URL for the city search API request
        url = f'{BASE_URL}search.json?key={API_KEY}&q={query}'
        
        # Send a GET request to the API
        response = requests.get(url)
        
        # Check for HTTP status errors
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error searching for cities: {str(e)}")
        return None

# Function to display weather data
def display_weather(weather_data):
    """
    Display weather data for a city.
    
    Args:
        weather_data (dict): Weather data for a city.
    """
    # Extract and display relevant weather information
    current_weather = weather_data['current']
    
    print(f"Temperature: {current_weather['temp_c']}°C")
    print(f"Condition: {current_weather['condition']['text']}")

# Function to display 14-day weather forecast
def display_14_day_forecast(forecast_data):
    """
    Display a 14-day weather forecast for a city.
    
    Args:
        forecast_data (dict): Weather forecast data for a city.
    """
    for day in forecast_data['forecast']['forecastday']:
        print(f"Date: {day['date']}")
        print(f"Condition: {day['day']['condition']['text']}")
        print(f"High Temperature: {day['day']['maxtemp_c']}°C")
        print(f"Low Temperature: {day['day']['mintemp_c']}°C")
        print("---------------")

# Function to display astronomy data
def display_astronomy_data(astronomy_data):
    """
    Display astronomy data for a location.
    
    Args:
        astronomy_data (dict): Astronomy data for a location.
    """
    location = astronomy_data['location']
    astronomy = astronomy_data['astronomy']

    print(f"Weather in {location['name']}, {location['region']}, {location['country']}:")
    print(f"Sunrise: {astronomy['astro']['sunrise']}")
    print(f"Sunset: {astronomy['astro']['sunset']}")
    print(f"Moonrise: {astronomy['astro']['moonrise']}")
    print(f"Moonset: {astronomy['astro']['moonset']}")
    print(f"Moon Phase: {astronomy['astro']['moon_phase']}")
    print(f"Moon Illumination: {astronomy['astro']['moon_illumination']}%")
    print(f"Is Moon Up: {'Yes' if astronomy['astro']['is_moon_up'] else 'No'}")
    print(f"Is Sun Up: {'Yes' if astronomy['astro']['is_sun_up'] else 'No'}")

# Function to display historical weather data
def display_historical_weather(historical_data):
    """
    Display historical weather data for a city.
    
    Args:
        historical_data (dict): Historical weather data for a city.
    """
    location = historical_data['location']
    forecast = historical_data['forecast']['forecastday'][0]  # Assuming data is for a single day

    print(f"Weather history in {location['name']}, {location['region']}, {location['country']} on {forecast['date']}:")
    print(f"Max Temperature: {forecast['day']['maxtemp_c']}°C")
    print(f"Min Temperature: {forecast['day']['mintemp_c']}°C")
    print(f"Average Temperature: {forecast['day']['avgtemp_c']}°C")
    print(f"Max Wind Speed: {forecast['day']['maxwind_kph']} km/h")
    print(f"Total Precipitation: {forecast['day']['totalprecip_mm']} mm")
    print(f"Average Visibility: {forecast['day']['avgvis_km']} km")
    print(f"Average Humidity: {forecast['day']['avghumidity']}%")
    print(f"Condition: {forecast['day']['condition']['text']}")

# Function to display the weather of favorite cities
def display_favorite_weather(favorite_cities):
    """
    Display weather for favorite cities.
    
    Args:
        favorite_cities (list): List of favorite city names.
    """
    if favorite_cities:
        print("\nFavorite Cities:")
        for city in favorite_cities:
            weather_data = get_current_weather(city)
            if weather_data:
                print(f"{city}:")
                display_weather(weather_data)
    else:
        print("No favorite cities yet.")

# Menu-driven interface
def menu():
    favorite_cities = load_from_file("favorites.json")
    
    # Display weather for favorite cities at the beginning of the menu
    display_favorite_weather(favorite_cities)
    
    while True:
        print("\nMenu:")
        print("1. Get current weather")
        print("2. Get 14-day weather forecast")
        print("3. Get historical weather data")
        print("4. Get astronomy data")
        print("5. Add a city to favorites")
        print("6. Remove a city from favorites")
        print("7. List favorite cities with weather")
        print("8. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")
        
        if choice == '1':
            city = input("Enter city name: ")
            weather_data = get_current_weather(city)
            if weather_data:
                display_weather(weather_data)
            else:
                print(f"Error: Could not find weather data for '{city}'")
        elif choice == '2':
            city = input("Enter city name for forecast: ")
            weather_data = get_14_day_forecast(city)
            if weather_data:
                display_14_day_forecast(weather_data)
            else:
                print(f"Error: Could not find weather forecast data for '{city}'")
        elif choice == '3':
            city = input("Enter city name for historical data: ")
            date = input("Enter date (YYYY-MM-DD): ")
            weather_data = get_historical_weather(city, date)
            if weather_data:
                display_historical_weather(weather_data)
            else:
                print(f"Error: Could not find historical weather data for '{city}' on {date}")
        elif choice == '4':
            city = input("Enter city name for astronomy data: ")
            astronomy_data = get_astronomy_data(city)
            if astronomy_data:
                display_astronomy_data(astronomy_data)
            else:
                print(f"Error: Could not find astronomy data for '{city}'")
        elif choice == '5':
            city = input("Enter city name to add to favorites: ")
            favorite_cities, added = add_favorite(city, favorite_cities)
            if added:
                save_to_file("favorites.json", favorite_cities)
                print(f"{city} added to favorites.")
            else:
                print(f"{city} is already in favorites.")
        elif choice == '6':
            city = input("Enter city name to remove from favorites: ")
            favorite_cities = remove_favorite(city, favorite_cities)
            save_to_file("favorites.json", favorite_cities)
            print(f"{city} removed from favorites.")
        elif choice == '7':
            list_favorites(favorite_cities)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    menu()
