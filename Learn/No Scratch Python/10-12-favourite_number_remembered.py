import json


def store_favourite_number(filename):
    """Store the user's favourite number."""
    favourite_number = input("What is your favourite number? ")
    with open(filename, "w") as f_obj:
        json.dump(favourite_number, f_obj)


def retrive_favourite_number(filename):
    """Retrive the user's favourite number if available"""
    try:
        with open(filename) as f_obj:
            favourite_number = json.load(f_obj)
    except FileNotFoundError:
        store_favourite_number(filename)
    else:
        return favourite_number


def favourite_number_remembered():
    """Print user's favourite number"""
    filename = "Learn/No Scratch Python/favourite_number.json"
    favourite_number = retrive_favourite_number(filename)
    if favourite_number:
        print(f"I know what your favourite number is! It's {favourite_number}!")


favourite_number_remembered()
