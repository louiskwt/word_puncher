import random

def punch_out_words(lines):
    for index in range(len(lines)):
        word_lst = lines[index].split()
        if len(word_lst) > 2:
            random_word_index = random.randint(2, len(word_lst)-1)
            word_lst[random_word_index] = replace_word_with_blank(word_lst[random_word_index])
        lines[index] = " ".join(word_lst)
    return lines

def replace_word_with_blank(word):
    return "_" * len(word) * 2