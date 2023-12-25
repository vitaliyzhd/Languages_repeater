from german_words import deutsch1

import random

print("Welcome to language repeater!\n")


def remove_double_quotes(deutsch1):
    """The function converts a dictionary into a list"""
    empty_dictionary = {}
    for key, value in deutsch1.items():
        if isinstance(value, str):
            empty_dictionary[key] = value.strip('')
        else:
            empty_dictionary[key] = value
    return empty_dictionary


def input_trouble():
    correct_translation = False
    while not correct_translation:
        true_german_word = input("\nTry to remember and type again: ")
        if true_german_word == "?":
            print(random_key)
            input("Type this word to memorise better: ")
        elif true_german_word == random_key:
            print("Good! You remembered this word")
            correct_translation = True


deutsch1_dictionary = remove_double_quotes(deutsch1)

should_continue = True
for word in deutsch1_dictionary:
    random_key = random.choice(list(deutsch1_dictionary.keys()))
    random_value = deutsch1_dictionary[random_key]
    print(f"\nTranslate this word: {random_value}\nType 'STOP' to finish revising")

    german_word = input()
    if german_word == random_key:
        print("Good job. Next word:\n")

    elif german_word == "STOP":
        should_continue = False

    elif german_word == "?":
        print(random_key)
        input("Type this word to memorise better: ")

    else:
        input_trouble()
