import json

filename = "Learn/No Scratch Python/favourite_number.json"

with open(filename) as f_obj:
    favourite_number = json.load(f_obj)
    print(f"I know your favourite number! It's {favourite_number}")