def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")


filenames = [
    "Learn/No Scratch Python/alice.txt",
    "Learn/No Scratch Python/siddhartha.txt",
    "Learn/No Scratch Python/moby_dick.txt",
    "Learn/No Scratch Python/little_women.txt",
]

for filename in filenames:
    count_words(filename)