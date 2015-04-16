import random
from sys import argv

script, filename = argv

filename = open(filename)

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    key_tup = tuple()
    text = corpus.read()
    poem_word = text.rstrip().replace(",", "").replace("?", "").split()
    last_words = poem_word[-2] + " " + poem_word[-1]
    poem_dict = {}
    for i in range(len(poem_word) - 2):
        key_tup = (poem_word[i], poem_word[i + 1]) 
        if (poem_dict.get(key_tup) == None):
            poem_dict[key_tup] = [poem_word[i + 2]]
        else:
            poem_dict[key_tup].append(poem_word[i + 2])
    return poem_dict, last_words


def make_text(chains, last_words):
    """Takes dictionary of markov chains; returns random text."""
    start_words = random.choice(chains.keys())
    second_word = random.choice(chains[start_words])
    w1 = start_words[1]
    w2 = second_word
    
    gen_words = []
    while True:
        gen_words.append(w1)
        w1, w2 = w2, random.choice(chains[w1, w2])
        if w1 + " " + w2 == last_words:
            break
    gen_words.append(w2)
    print ' '.join(gen_words)




input_text = "Some text"

# Get a Markov chain
chain_dict, last_words = make_chains(filename)

# Produce random text
random_text = make_text(chain_dict, last_words)

