from stats import count_words, count_chars


def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()


def main():
  text = get_book_text("./books/frankenstein.txt")
  wc = count_words(text)
  cc = count_chars(text)

  print(f"{wc} words found in the document")
  print(cc)


main()
