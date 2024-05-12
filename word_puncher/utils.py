import random, string

COMMON_WORDS = {
    'articles': ['a', 'an', 'the'],
    'personal_pronouns': ['he', 'i', 'she', 'they', 'we', 'you', "he's", "i'm", "she's", "they're", "we're", "you're"],
    'demonstrative_pronouns': ['that', 'these', 'this', 'those'],
    'interrogative_pronouns': ['what', 'which', 'who', 'whom', 'whose']
}

def punch_out_words(lines):
    answer_keys = []
    for index in range(len(lines)):
        word_lst = lines[index].split()
        if len(word_lst) > 2:
            random_word_index = random.randint(2, len(word_lst)-1)
            target_word = word_lst[random_word_index]
            is_common_word = check_for_common_words(strip_punctuations(target_word))
            while is_common_word:
                random_word_index = random.randint(2, len(word_lst)-1)
                target_word = word_lst[random_word_index]
                is_common_word = check_for_common_words(strip_punctuations(target_word)) 
            if not is_common_word:
                answer_keys.append(target_word)
                word_lst[random_word_index] = replace_word_with_blank(word_lst[random_word_index])
        lines[index] = " ".join(word_lst)
    return [lines, answer_keys]

def replace_word_with_blank(word):
    return "_" * len(word) * 2

def strip_punctuations(word):
    """
    A function that strips punctuation at the beginning or end of a word
    >>> word1 = "'Hey!'"
    >>> strip_punctuations(word1)
    'Hey'
    >>> word2 = "This's?"
    >>> strip_punctuations(word2)
    "This's"
    """
    new_word = word
    while new_word[0] in string.punctuation or new_word[-1] in string.punctuation:
        if new_word[0] in string.punctuation:
            new_word = new_word[1:]
        if new_word[-1] in string.punctuation:
            new_word = new_word[:-1]
    return new_word


def check_for_common_words(word):
    """
    A function that check whether a word is a common word in English
    >>> a = "a"
    >>> check_for_common_words(a)
    True
    >>> foo = "foo"
    >>> check_for_common_words(foo)
    False
    >>> p = "He's"
    >>> check_for_common_words(p)
    True
    """
    return any([strip_punctuations(word.lower()) in COMMON_WORDS[key] for key in COMMON_WORDS])
