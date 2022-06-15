"""
Author: O. Smit

Description:

Simulates a stripped down version of the hacking mini-game
from the Fallout series. This revolves around figuring out
a password with a few guesses. After each guess information
about how many letters match the password (same letter in the same place)
is given. The list of possible right answers is narrowed down
accordingly.

NB: this script is not at all finished.
"""


from random import randint
import hacking_tests


def compare_and_sort_words(list_of_words, length):
    scores = {}
    for i in range(0, length):
        scores[i] = []

    for index in range(0, len(list_of_words)):
        word = list_of_words[index]

        for next_word in range(index + 1, len(list_of_words)):
            compare_word = list_of_words[next_word]
            score = 0

            for letter in range(0, length):
                test = word[letter] == compare_word[letter]
                if test is True:
                    score += 1
            scores[score].append(f"{word}-{compare_word}")

    return scores


def compute_score(list_of_words, length):
    for index in range(0, len(list_of_words)):
        word = list_of_words[index]

        for next_word in range(index + 1, len(list_of_words)):
            compare_word = list_of_words[next_word]
            score = 0

            for letter in range(0, length):
                test = word[letter] == compare_word[letter]
                if test is True:
                    score += 1
    return score


def main():
    amount = int(input("How many words will there be?\n> "))
    length = int(input("How many letters will there be in each word?\n> "))
    list_of_words = []

    word_space = open("words.txt")
    for word in word_space:
        list_of_words.append(word.strip())

    password = list_of_words[randint(1, len(list_of_words) - 1)]

    print(f"Possible answers:\n{'  '.join(list_of_words)}\n")

    all_words_compared = compare_and_sort_words(list_of_words, length)
    print("How many letters in the same place:")
    for key, value in all_words_compared.items():
        print(f"{key}/{length}\t{value}")

    guess_counter = 0

    while guess_counter < len(list_of_words) - 1:
        guess = input("\nYour guess: ")
        guess_counter += 1
        if guess != password:
            guess_comparison = [guess, password]
            guess_score = compute_score(guess_comparison, length)
            print(f"Score: ", end='')
            print(f"{guess_score}/{length}\t{all_words_compared[guess_score]}")
        else:
            break
    if guess == password:
        print(f"Hurray! You found the password: '{password}'")
        if guess_counter > 1:
            print(f"It took you: {guess_counter} guesses!")
        else:
            print(f"It took you: {guess_counter} guess!")
    else:
        print("Alas, you ran out of guesses!")

    play_again = input("\nWould you like to play again? \
Type 'yes' or 'no'\n> ")
    return play_again


play_again = 'yes'

while play_again == 'yes':
    play_again = main()
