# Created by Daniel Smith
# DanielSmith.co
# Dependencies: NLTK
# Python 3.6 with itertools library
# MIT License 2018


import itertools
from time import *
import time
import nltk
nltk.download('words')
english_vocab = set(w.lower() for w in nltk.corpus.words.words())
def anagram(phrase):
    startTime = time.time()
    moves = 0
    phrase = phrase.lower()
    phrase = phrase.replace(" ", "")
    words = []
    for p in itertools.permutations(phrase):
        possibleWord = ''.join(p)

        if possibleWord in english_vocab:
            if possibleWord != phrase and possibleWord not in words:
                words.append(possibleWord)

        print(p)
        moves += 1

    endTime = time.time()

    print("Time taken (seconds): {}".format((endTime - startTime)))
    print("{} Possible permutations of {}".format(moves, phrase))
    print(words)