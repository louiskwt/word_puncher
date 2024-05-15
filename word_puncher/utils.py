import random, string

COMMON_WORDS = {
    'articles': ['a', 'an', 'the'],
    'personal_pronouns': ['he', 'i', 'it', 'she', 'they', 'we', 'you', "he'd", "it'd", "she'd", "i'd", "they'd", "we'd", "you'd", "he's", "it's", "i'm", "she's", "they're", "we're", "you're", "i've", "they've", "we've", "you've"],
    'demonstrative_pronouns': ['that', 'these', 'this', 'those', "that's", "these're", "this's", "those're", "that'd", "these'd", "this'd", "those'd"],
    'interrogative_pronouns': ['what', 'which', 'who', 'whom', 'whose', "what'd", "which'd", "who'd", "what's", "which's", "who's", "what're", "which're", "who're", "what've", "which've", "who've"]
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
    stripped_word = strip_punctuations(word)

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

def find_punctuation(word):
    """
    A function that extract punctuation at the beginning and end of a word
    >>> word1 = "'(Hey!)'"
    >>> punctuations = find_punctuation(word1)
    >>> punctuations["front"]
    "'("
    >>> punctuations["end"]
    "!)'"
    """
    punctuation_table = { "front": "", "end": "" }
    target = word
    while target[0] in string.punctuation or target[-1] in string.punctuation:
        if target[0] in string.punctuation:
            punctuation_table["front"] += target[0]
            target = target[1:]
        if target[-1] in string.punctuation:
            punctuation_table["end"] += target[-1]
            target = target[:-1]
    punctuation_table['end'] = punctuation_table["end"][::-1]
    return punctuation_table


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
