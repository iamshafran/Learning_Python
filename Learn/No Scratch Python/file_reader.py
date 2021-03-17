filename = "/Users/iamshafran/Development/Python/Learn/No Scratch Python/pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())