import random, string

COMMON_WORDS = {
    'articles': ['a', 'an', 'the'],
    'personal_pronouns': ['he', 'i', 'it', 'she', 'they', 'we', 'you', "he'd", "it'd", "she'd", "i'd", "they'd", "we'd", "you'd", "he's", "it's", "i'm", "she's", "they're", "we're", "you're", "i've", "they've", "we've", "you've"],
    'demonstrative_pronouns': ['that', 'these', 'this', 'those', "that's", "these're", "this's", "those're", "that'd", "these'd", "this'd", "those'd"],
    'interrogative_pronouns': ['what', 'which', 'who', 'whom', 'whose', "what'd", "which'd", "who'd", "what's", "which's", "who's", "what're", "which're", "who're", "what've", "which've", "who've"]
}

def punch_out_words(lines, word_len=1):
    answer_key = []
    for index in range(len(lines)):
        inline_word_lst = lines[index].split()
        if len(inline_word_lst) > 2:
            targets = find_random_words(inline_word_lst, word_len)
            target_keys = targets.keys()
            answer_key.append(" ".join([targets[k] for k in target_keys]))
            for i, word in targets.items():
                punctuations_in_word = find_punctuation(inline_word_lst[i])
                inline_word_lst[i] = punctuations_in_word["front"] + replace_word_with_blank(word) + punctuations_in_word['end'] 
            inline_word_lst.insert(min(list(target_keys), key=lambda s: int(s)), "(" + str(index+1) +".)")
        lines[index] = " ".join(inline_word_lst)
    return [lines, format_answer_key(answer_key)]

def extract_words(text):
    """
        a util function return a list containing list of words for each line
        >>> text = ["Hello, friends", "How are you?", "Awesome! And you."]
        >>> extracted_words = extract_words(text) 
        >>> extracted_words
        [['Hello', 'friends'], ['How', 'are', 'you'], ['Awesome', 'And', 'you']]
    """
    return [[strip_punctuations(word) for word in line.split(" ")] for line in text]


def find_random_words(word_lst, word_len=1, linked=True):
    target_word_index, targets, count = random.randint(2, len(word_lst)-1), {}, 0
    while count < word_len:
        target_word = word_lst[target_word_index]
        in_common_words = check_for_common_words(strip_punctuations(target_word))
        while in_common_words:
            target_word_index = random.randint(2, len(word_lst)-1)
            target_word = word_lst[target_word_index]
            in_common_words = check_for_common_words(strip_punctuations(target_word))
        targets[target_word_index] = strip_punctuations(target_word)
        if linked:
            target_word_index = target_word_index+1 if target_word_index + 1 != len(word_lst) else target_word_index-1
        else:
            target_word_index = random.randint(2, len(word_lst)-1) 
        count += 1
    return targets

def format_answer_key(answer_key):
    """ a util function that format the answer key with index"""
    return [str(i+1) + "." + " " + answer_key[i] for i in range(len(answer_key))]

def replace_word_with_blank(word):
    """
    A function that replaces word with _____ but keeps the punctuations
    >>> replace_word_with_blank("Hello!")
    '__________!'
    >>> replace_word_with_blank("(Hey!)")
    '(______!)'
    """
    stripped_word = strip_punctuations(word)
    punctuations = find_punctuation(word) 
    if stripped_word != word:
        return punctuations['front'] + ('_' * len(stripped_word) * 2) + punctuations['end']
    else:
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
