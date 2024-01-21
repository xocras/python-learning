country_entry = input("Add country name: ")
visits_entry = int(input("Add number of visits: "))
list_of_cities = eval(input("Enter a list from formatted string: "))

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, visits, cities):
    log = {"country": country,
           "visits": visits,
           "cities": cities}

    travel_log.append(log)


add_new_country(country_entry, visits_entry, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
