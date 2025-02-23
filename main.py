from stats import number_of_words
from stats import number_of_letters
from stats import sort_dict

def main():
    path = 'books/frankenstein.txt'
    book = get_book_text(path)
    num_words = number_of_words(book)
    num_letters = number_of_letters(book)
    print(num_words)
    print(num_letters)
    sort_dict(num_letters)

def get_book_text(filepath):
    with open(filepath) as p:
        text = p.read()
    return text

main()
