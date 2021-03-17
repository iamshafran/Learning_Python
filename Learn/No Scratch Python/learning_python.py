filename = "Learn/No Scratch Python/learning_python.txt"
file_list = []

with open(filename) as file_object:
    contents = file_object.read()
    print("\n Read entire file:")
    print(contents.rstrip())

with open(filename) as file_object:
    print("\n Read file with for loop:")
    for line in file_object:
        print(line.rstrip())
        file_list.append(line)

print("\n Read file from list:")
for item in file_list:
    print(item.rstrip())

print("\n Replacing 'Python' with 'C':")
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.replace("Python", "C").rstrip())