from trienode import TrieNode

WORDS = "./frequency_dictionary_en_82_765.txt"
BIGRAMS = "./frequency_bigramdictionary_en_243_342.txt"

def initialize_dictionary():
    dictionary = TrieNode()
    for word in open(WORDS, "rt").read().split('\n'):
        dictionary.insert( word.split()[0] )
    return dictionary

def initialize_word_count():
    word_count = {}
    for word in open(WORDS, "rt").read().split('\n'):
        word_count[word.split()[0]] = int(word.split()[1])
    return word_count

def initialize_bigram_count():
    bigram_count = {}
    for bigram in open(BIGRAMS, "rt").read().split('\n'):
        if bigram:
            bigram_splitted = bigram.split(' ')
            bigram_count[(bigram_splitted[0], bigram_splitted[1])] = int(bigram_splitted[2])
    return bigram_count
