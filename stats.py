def count_words(words):
    word_list = words.split()
    return len(word_list)

def count_char(words):
    lower_case_words = words.lower()
    count_dict = {}
    for char in lower_case_words:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict

def sort_on(some_dict):
    return some_dict["num"]

def sort_dict(words_dict):
    new_list = []
    for key, value in words_dict.items():
        new_list.append({"char": key, "num": value})
    new_list.sort(reverse = True, key=sort_on)
    return new_list