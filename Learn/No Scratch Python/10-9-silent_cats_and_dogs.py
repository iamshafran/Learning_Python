filenames = ["Learn/No Scratch Python/cats.txt", "Learn/No Scratch Python/dogs.txt"]

for filename in filenames:
    try:
        with open(filename) as f_Obj:
            contents = f_Obj.read()
    except FileNotFoundError:
        continue
    else:
        print(contents)