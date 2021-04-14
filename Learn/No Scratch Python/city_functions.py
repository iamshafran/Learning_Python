def get_city_country(city, country, population=""):
    if population:
        formatted_city_country = f"{city}, {country} - population {population}"
    else:
        formatted_city_country = f"{city}, {country}"
    return formatted_city_country