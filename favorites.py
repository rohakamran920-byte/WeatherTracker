```python
import json
import os

FILE_NAME = "data/recent.json"


def create_file():
    """
    Create the JSON file if it does not exist.
    """
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)


def get_favorites():
    """
    Return all favorite cities.
    """
    create_file()

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def add_favorite(city):
    """
    Add a city to favorites.
    """
    create_file()

    favorites = get_favorites()

    if city not in favorites:
        favorites.append(city)

        with open(FILE_NAME, "w") as file:
            json.dump(favorites, file, indent=4)


def remove_favorite(city):
    """
    Remove a city from favorites.
    """
    create_file()

    favorites = get_favorites()

    if city in favorites:
        favorites.remove(city)

        with open(FILE_NAME, "w") as file:
            json.dump(favorites, file, indent=4)
```
