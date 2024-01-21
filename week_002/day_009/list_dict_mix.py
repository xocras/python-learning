# Nesting Dictionaries in Lists
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
    {
        "country": "Italy",
        "cities_visited": ["Rome", "Florence", "Venice"],
        "total_visits": 8,
    },
    {
        "country": "Japan",
        "cities_visited": ["Tokyo", "Osaka", "Kyoto"],
        "total_visits": 10,
    },
    {
        "country": "Canada",
        "cities_visited": ["Toronto", "Vancouver", "Montreal"],
        "total_visits": 3,
    },
    {
        "country": "Australia",
        "cities_visited": ["Sydney", "Melbourne", "Brisbane"],
        "total_visits": 7,
    },
]

for entry in travel_log:
    print(entry)
    