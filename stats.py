def sort_dict(num_letters_dict):
    sorted_items = sorted(num_letters_dict.items(), key=lambda item: item[1], reverse=True)
    sorted_dict = {key: value for key, value in sorted_items}
    return sorted_dict

def number_of_letters(text):
    lower_text = text.lower()
    letter_dict = {}
    for char in lower_text:
        if char.isalpha():
            if char in letter_dict:
                letter_dict[char] += 1
            else:
                letter_dict[char] = 1
    return letter_dict

def number_of_words(text):
    words = text.split()
    return len(words)
