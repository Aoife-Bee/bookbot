import sys

def get_book_text(argv):
    with open(argv) as f:
        return f.read()

from stats import get_num_words

from stats import get_num_characters

from stats import sort_character_counts

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    else: 
        book = get_book_text(argv=sys.argv[1])
        word_count = get_num_words(book)
        character_count = get_num_characters(book)
        sorted_character_count = sort_character_counts(character_count)
        print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}
----------- Word Count ----------""")
        print(f"""Found {word_count} total words
--------- Character Count -------""")
        for entry in sorted_character_count:
         if entry["char"].isalpha():
               print(f"{entry['char']}: {entry['num']}")
        print("============= END ===============")

main()