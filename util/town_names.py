import geonamescache
import random


def generate_european_town():
    gc = geonamescache.GeonamesCache()
    countries = gc.get_countries_by_names()
    europe = {name: info for name, info in countries.items() if info['continentcode'] == 'EU'}
    europe_codes = {info['iso']: info for info in europe.values()}
    cities = gc.get_cities()
    european_cities = {id: city for id, city in cities.items() if city['countrycode'] in europe_codes.keys()}
    random_city = random.choice(list(european_cities.values()))
    return random_city['name']


towns = ["Transylvania", "Salem", "Whitby", "Derry", "Bran", "Sleepy Hollow", "Castle Dracula", "Arkham", "Innsmouth",
         "Silent Hill", "Ravenswood", "Midwich", "Haddonfield", "Amityville", "Bates Motel"]


def get_town():
    index = random.randint(0, len(towns) - 1)
    return towns[index]
