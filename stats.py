def sort_dict(num_letters_dict):
    pass

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
    count = 0
    for word in words:
        if word in words:
            count += 1
    return count
