from stats import count_words, count_char, sort_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_book = sys.argv[1]
    words_in_text = count_words(get_book_text(path_to_book))
    char_in_text = count_char(get_book_text(path_to_book))
    sorted_list = sort_dict(char_in_text)
    print("============ BOOKBOT ============ \n"
          "Analyzing book found at books/frankenstein.txt...\n"
          "----------- Word Count ----------")
    print(f"Found {words_in_text} total words")
    print("--------- Character Count -------")
    for dicts in sorted_list:
        if dicts["char"].isalpha():
            print(f"{dicts["char"]}: {dicts["num"]}")
    print("============= END ===============")

main()