def get_book_text(filepath):
  with open(filepath) as f:
    return f.read()


def count_words(text):
  return len(text.split())

def main():
  text = get_book_text("./books/frankenstein.txt")
  wc = count_words(text)

  print(f"{wc} words found in the document")

main()
