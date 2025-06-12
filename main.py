from stats import count_words, count_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    path_to_frankenstein = "books/frankenstein.txt"
    print(f"{count_words(get_book_text(path_to_frankenstein))} words found in the document")
    print(count_char(get_book_text(path_to_frankenstein)))
main()