from stats import get_num_words, get_num_char
import sys

def main(file_path):
   file_path = file_path
   num_words = get_num_words(file_path)
   num_char = get_num_char(file_path)
   output(file_path, num_words, num_char)

def output(file_path, num_words, num_char):
   print("============ BOOKBOT ============")
   print(f"Analyzing book found at {file_path}...")
   print(f"----------- Word Count ----------")
   print(f"Found {num_words} total words")
   print(f"--------- Character Count -------")
   for char in num_char:
      if char["char"].isalpha():
        print(f"{char["char"]}: {char["num"]}")


if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])