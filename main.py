def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)

    num_words = number_of_words(text)
    print(f"{num_words} words found in the text\n")

    num_letters = number_of_letters(text)
    sort_dict(num_letters)

    print("--- End Report ---")

def sort_dict(dict):
    char_list = [{"char": char, "num": count} for char, count in dict.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)

    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

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