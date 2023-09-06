def check_input(list):
  inp = input("Give me a word ")
  while inp not in list:
    inp = input("Try again ")
  return inp