def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def get_num_words(file_path):
    file_contents = get_book_text(file_path)
    list_of_words = file_contents.split()
    word_count = len(list_of_words)
    print(f"{word_count} words found in the document")

def sort_on():
    return dict["num"]



def get_num_char(file_path):
    file_contents = get_book_text(file_path).lower()
    list_of_chars = list(file_contents)
    letter_count = {}
    for letter in list_of_chars:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
   
    print(letter_count)
