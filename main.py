def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text_(book_path)
    get_word_count(text)
    print(f"{get_word_count(text)} words found in the book.")
    get_chars_count(text)


def get_book_text_(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_chars_count(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    print(chars)


main()
