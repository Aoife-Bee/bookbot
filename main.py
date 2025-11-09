def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

from stats import get_num_words

from stats import get_num_characters

from stats import sort_character_counts

def main():
    frankenstein_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(frankenstein_text)
    character_count = get_num_characters(frankenstein_text)
    sorted_character_count = sort_character_counts(character_count)
    # python
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------""")
    for entry in sorted_character_count:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()