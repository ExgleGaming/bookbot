import sys
from stats import number_of_words
from stats import number_of_letters
from stats import sort_dict

def main():
    path = sys.argv
    book = get_book_text(path)
    num_words = number_of_words(book)
    num_letters = number_of_letters(book)
    sorted_dict = sort_dict(num_letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as p:
        text = p.read()
    return text

main()
