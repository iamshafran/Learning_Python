from datetime import datetime

filename = "Learn/No Scratch Python/guest_book.txt"

while True:
    timeOfEntry = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    name = input("Please enter your name: ")
    print(f"Hi {name}, welcome! Your details have been recorded.")

    with open(filename, "a") as file_object:
        file_object.write(f"{timeOfEntry} - {name}\n")