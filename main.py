import sys
from stats import (
  get_num_words,
  get_num_char,
  report
)

def main():
  if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_text = get_book_text(sys.argv[1])
  word_count = get_num_words(book_text)
  char_count = get_num_char(book_text)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")
  for char in report(char_count):
    print(f"{char["char"]}: {char["num"]}")

def get_book_text(filepath):
  with open(filepath) as f:
    book_contents = f.read()
    return(book_contents)

main()
