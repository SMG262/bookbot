import json


def count_words(text):
    split_words = text.split()
    return len(split_words)
    
def count_characters2(text):
    dictionary = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0, 'æ': 0, 'â': 0, 'ê': 0, 'ë': 0, 'ô': 0}
    dict_list = []
    lower_case = text.lower()
    for c in lower_case:
        if c in dictionary:
            dictionary[c] += 1
    sorted_dict = sorted(dictionary.items(), reverse=True, key=lambda x:x[1])
    converted_dict = dict(sorted_dict)
    result = "\n".join([f"{key}: {value}" for key, value in converted_dict.items()])
    return result