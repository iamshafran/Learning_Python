filenames = ["Learn/No Scratch Python/cats.txt", "Learn/No Scratch Python/dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as f_Obj:
            contents = f_Obj.read()
    except FileNotFoundError:
        print("One of the specified file is missing.")
    else:
        print(contents)