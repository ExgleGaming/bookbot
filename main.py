def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    num_words = number_of_words(text)
    print(f"{num_words} words found in the text")
    num_letters = number_of_letters(text)
    sort_on(num_letters)

def sort_on(dict):
    
    for key, value in dict:
        print(f"The {key} character was found {value} times")

def number_of_letters(text):
    lowered_letters = text.lower()
    char_count = {}

    for char in lowered_letters:
        if char.isalpha(): 
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def number_of_words(text):
    words = text.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        return f.read()
    

main()