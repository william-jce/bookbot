def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text_(book_path)
    chars_dict = get_char_count(text)
    sorted_letters = get_sorted_letters(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_word_count(text)} words found in the book.")
    
    for item in sorted_letters:
        if item["char"].isalpha():
            print(f"The '{item['char']} character was found {item['num']} times.")

    print("--- End report ---")


def get_book_text_(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    chars = {}
    for t in text:
        lowered = t.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_sorted_letters(chars):
    letters = []
    for char in chars:
        letters.append({"char": char, "num": chars[char]})
    sorted_letters = sorted(letters, reverse=True, key=lambda sort: sort["num"])
    return sorted_letters


main()
