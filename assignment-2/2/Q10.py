import random

all_words = "all the words in the world".split()

def get_random_word():
    return random.choice(all_words)

def get_unique_words():
    unique_words = set()
    for _ in range(1000):
        unique_words.add(get_random_word())
    return unique_words

print(get_unique_words())