import json

# Create an empty list to store favorite cities
favorite_cities = []

# Function to add a city to favorites
def add_favorite(city):
    favorite_cities.append(city)

# Function to remove a city from favorites
def remove_favorite(city):
    if city in favorite_cities:
        favorite_cities.remove(city)

# Function to list all favorite cities
def list_favorites():
    return favorite_cities

# Function to update a favorite city
def update_favorite(old_city, new_city):
    if old_city in favorite_cities:
        index = favorite_cities.index(old_city)
        favorite_cities[index] = new_city

# Function to save favorites to a JSON file
def save_to_file(filename):
    with open(filename, 'w') as file:
        json.dump(favorite_cities, file)

# Function to load favorites from a JSON file
def load_from_file(filename):
    try:
        with open(filename, 'r') as file:
            favorite_cities.extend(json.load(file))
    except FileNotFoundError:
        pass
