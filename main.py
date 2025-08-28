from stats import num_words
from stats import num_char

def main():
  frankenstein = get_book_text("./books/frankenstein.txt")
  print(f"{num_words(frankenstein)} words found in the document")
  frankenstein_char = num_char(frankenstein)
  print(frankenstein_char)

def get_book_text(filepath):
  with open(filepath) as f:
    book_contents = f.read()
    return(book_contents)

main()
