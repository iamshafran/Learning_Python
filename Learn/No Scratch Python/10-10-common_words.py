filename = "Learn/No Scratch Python/pride_and_prejudice.txt"

with open(filename) as f_obj:
    contents = f_obj.read()
    search_word = "the"
    word_count = contents.lower().count(search_word)
    print(
        f"The word '{search_word}' appears {word_count} times in the file '{filename}'"
    )
