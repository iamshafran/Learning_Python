print("Enter two numbers, I will add them together.")
print("Enter 'q' to exit program.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("I can only add two numbers, not letters or special characters.")
    else:
        print(answer)