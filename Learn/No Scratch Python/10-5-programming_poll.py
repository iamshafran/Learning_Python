filename = "Learn/No Scratch Python/programming_poll.txt"

answer = " "

while answer:
    answer = input("Why do you like programming? ")

    if answer == "0":
        break

    with open(filename, "a") as file_object:
        file_object.write(f"{answer}\n")
