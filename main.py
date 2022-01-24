import urllib.request
from collections import Counter


def find_words(
    current_guess: list,
    dict_words: str,
    letters_in_word: list,
    letters_not_in_word: list,
) -> list:
    words = [
        word
        for word in dict_words
        if len(word) == 5
        and is_possible_guess(word, current_guess, letters_in_word, letters_not_in_word)
    ]

    return words


def is_possible_guess(
    word: str, current_guess: list, letters_in_word: list, letters_not_in_word: list
) -> bool:
    word_counter = Counter(word)
    for letter in letters_in_word:
        if letter not in word or word_counter[letter] < letters_in_word[letter]:
            return False

    for guess, letter in zip(current_guess, word):
        if guess["correct_position"] and guess["letter"] != letter:
            return False

        if not guess["correct_position"] and guess["letter"] == letter:
            return False

        if letter in letters_not_in_word:
            return False

    return True


with urllib.request.urlopen(
    "https://raw.githubusercontent.com/InnovativeInventor/dict4schools/master/safedict_full.txt"
) as safe_words_file:
    words = safe_words_file.read().decode("utf-8").split()


guesses = [
    [
        {
            "letter": "h",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "a",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "p",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "p",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "y",
            "correct_position": False,
            "in_word": False,
        },
    ],
    [
        {
            "letter": "w",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "o",
            "correct_position": False,
            "in_word": True,
        },
        {
            "letter": "r",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "k",
            "correct_position": False,
            "in_word": True,
        },
        {
            "letter": "s",
            "correct_position": False,
            "in_word": False,
        },
    ],
    [
        {
            "letter": "b",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "l",
            "correct_position": False,
            "in_word": True,
        },
        {
            "letter": "o",
            "correct_position": True,
            "in_word": True,
        },
        {
            "letter": "c",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "k",
            "correct_position": False,
            "in_word": True,
        },
    ],
]

letters_not_in_word = ["h", "a", "p", "y", "w", "r", "s", "b", "c"]
letters_in_word = {
    "o": 1,
    "k": 1,
    "l": 1,
}


print(find_words(guesses[2], words, letters_in_word, letters_not_in_word))
