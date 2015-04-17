import random
from sys import argv

class SimpleMarkovGenerator(object):

    # def __init__(self, filename):
    #     self.filename = filename

    def read_text(self, corpus):
        """Takes input text as string; returns dictionary of markov chains."""
        poem_word = corpus.rstrip().replace(",", "").replace("?", "").split()
        return poem_word

    def make_chains(self, poem_word):
        last_words = poem_word[-2] + " " + poem_word[-1]
        poem_dict = {}
        for i in range(len(poem_word) - 2):
            key_tup = (poem_word[i], poem_word[i + 1]) 
            if (poem_dict.get(key_tup) == None):
                poem_dict[key_tup] = [poem_word[i + 2]]
            else:
                poem_dict[key_tup].append(poem_word[i + 2])
        return poem_dict, last_words

    def make_text(self, full_text):
        """Takes dictionary of markov chains; returns random text."""
        source = self.read_text(full_text)
        chains, last_words = self.make_chains(source)
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

if __name__ == "__main__":

    script, filename1, filename2 = argv
    file1 = open(filename1)
    file2 = open(filename2)
    text1 = file1.read()
    text2 = file2.read()
    full_text = text1 + text2
    ourrandomscript = SimpleMarkovGenerator()
    ourrandomscript.make_text(full_text) 
    ourrandomscript.make_text(full_text)
    ourrandomscript.make_text(full_text)
    ourrandomscript.make_text(full_text)
    ourrandomscript.make_text(full_text)