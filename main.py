from stats import count_words, count_char, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_frankenstein = "books/frankenstein.txt"
    words_in_text = count_words(get_book_text(path_to_frankenstein))
    char_in_text = count_char(get_book_text(path_to_frankenstein))
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