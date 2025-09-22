import sys

from stats import count_words, count_chars, rank_chars


def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()


def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]
  text = get_book_text(book_path)
  wc = count_words(text)
  cc = count_chars(text)
  rcc = rank_chars(cc)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  print("----------- Word Count ----------")
  print(f"Found {wc} total words")
  print("--------- Character Count -------")
  for k in rcc:
    if k.isalpha():
      print(f"{k}: {rcc[k]}")
  print("============= END ===============")


main()
