import json

filename = "Learn/No Scratch Python/favourite_number.json"

favourite_number = input("What is your favourite number? ")

with open(filename, "w") as f_obj:
    json.dump(favourite_number, f_obj)