import random

horror_locations = ["house", "apartment", "cabin", "hotel", "motel", "camp", "park", "wilderness", "town", "island",
                    "hospital", "asylum", "facility", "school", "university", "cemetery", "morgue", "church",
                    "monastery", "prison", "dungeon", "museum", "library"]


def get_horror_location():
    location = random.choice(horror_locations)

    return location
