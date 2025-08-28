import sys
from stats import num_words
from stats import num_char
from stats import report

def main():
  if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}")
  print("----------- Word Count ----------")
  print(f"Found {num_words(get_book_text(sys.argv[1]))} total words")
  print("--------- Character Count -------")
  for char in report(num_char(get_book_text(sys.argv[1]))):
    print(f"{char["char"]}: {char["num"]}")

def get_book_text(filepath):
  with open(filepath) as f:
    book_contents = f.read()
    return(book_contents)

main()
