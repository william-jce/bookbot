def num_words(book_text):
  return len(book_text.split())

def num_char(book_text):
  char_count = {}
  lowercase = book_text.lower()
  for char in lowercase:
    if char not in char_count:
      char_count[char] = 0
    char_count[char] += 1
  return char_count

def sort_enable(items):
  return items["num"]

def report(char_dict):
  sorted_dicts = []
  for char in char_dict:
    if char.isalpha():
      sorted_dicts.append({"char": char, "num": char_dict[char]})
  sorted_dicts.sort(reverse=True, key=sort_enable)
  return sorted_dicts
