travel_log = []

country_enter = input("please enter the name of the country:\n")
visits_enter = input("please enter how many times you've been to this country:\n")
cities_enter = eval(input("please enter the cities you like:\n"))

def new_country(country, visits, cities):
    add = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(add)
    print(f"I've been to {country} {visits} times.")
    print(f"My favorite city is {cities[0]}.")

new_country(country_enter, visits_enter, cities_enter)

