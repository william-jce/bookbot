def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text_(book_path)
    chars_dict = get_char_count(text)
    sorted_letters = get_sorted_letters(chars_dict)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{get_word_count(text)} words found in the book.")
    
    for item in sorted_letters:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']} character was found {item['num']} times.")

    print("--- End report ---")


def get_book_text_(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


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
    letters.sort(reverse=True, key=sort_on)
    return letters


main()
