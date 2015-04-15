import collections
import random
from sys import argv

script, filename = argv

filename = open(filename)

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    key_tup = tuple()
    text = corpus.read()
    poem_word = text.rstrip().split()
    poem_dict = {}
    for i in range(len(poem_word) - 2):
        key_tup = (poem_word[i], poem_word[i + 1]) 
        if (poem_dict.get(key_tup) == None):
            poem_dict[key_tup] = [poem_word[i + 2]]
        else:
            poem_dict[key_tup].append(poem_word[i + 2])

    return poem_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    start_word = random.choice(chains.keys())
    second_word = random.choice(chains[start_word])
    print start_word
    print second_word

    return "Here's some random text."



input_text = "Some text"

# Get a Markov chain
chain_dict = make_chains(filename)

# Produce random text
random_text = make_text(chain_dict)

print random_text
