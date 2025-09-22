def count_words(text):
  return len(text.split())


def count_chars(text):
  chars = {}
  for char in text.lower():
    chars[char] = chars.get(char, 0) + 1
  return chars
