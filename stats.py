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