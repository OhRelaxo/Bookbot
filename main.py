def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_words(words):
    word_count = 0
    word_list = words.split()
    for i in word_list:
        word_count += 1

    return word_count



def main():
    print(f"{get_words(get_book_text("books/frankenstein.txt"))} words found in the document")

main()