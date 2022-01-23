import urllib.request
from collections import Counter


def find_words(
    num_letters: int,
    current_guess: list,
    dict_words: str,
    letters_in_word: list,
    letters_not_in_word: list,
) -> list:
    words = [
        word
        for word in dict_words
        if len(word) == num_letters
        and is_possible_guess(word, current_guess, letters_in_word, letters_not_in_word)
    ]

    return words


def is_possible_guess(
    word: str, current_guess: list, letters_in_word: list, letters_not_in_word: list
) -> bool:
    word_counter = Counter(word)
    for letter in letters_in_word:
        if letter not in word or letters_in_word[letter] != word_counter[letter]:
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
            "letter": "w",
            "correct_position": True,
            "in_word": True,
        },
        {
            "letter": "e",
            "correct_position": False,
            "in_word": True,
        },
        {
            "letter": "e",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "k",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "s",
            "correct_position": False,
            "in_word": False,
        },
    ],
    [
        {
            "letter": "w",
            "correct_position": True,
            "in_word": True,
        },
        {
            "letter": "h",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "i",
            "correct_position": False,
            "in_word": True,
        },
        {
            "letter": "l",
            "correct_position": False,
            "in_word": False,
        },
        {
            "letter": "e",
            "correct_position": True,
            "in_word": True,
        },
    ],
]

letters_not_in_word = ["k", "s", "h", "l"]
letters_in_word = {
    "w": 1,
    "e": 1,
    "i": 1,
}


print(find_words(5, guesses[0], words, letters_in_word, letters_not_in_word))
