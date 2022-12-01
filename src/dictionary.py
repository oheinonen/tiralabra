from trienode import TrieNode

WORDS = "./frequency_dictionary_en_82_765.txt"
BIGRAMS = "./frequency_bigramdictionary_en_243_342.txt"

class Dictionary:
    def __init__(self):
        self._root = self.initialize_dictionary()
        self._word_count = self.initialize_word_count()
        self._bigram_count = self.initialize_bigram_count()
        self._total_words = sum(self._word_count.values())

    def initialize_dictionary(self):
        initial_node = TrieNode()
        with open(WORDS, "rt") as words:
            for word in words.read().split('\n'):
                initial_node.insert( word.split()[0] )
        return initial_node

    def initialize_word_count(self):
        word_count = {}
        with open(WORDS, "rt") as words:
            for word in words.read().split('\n'):
                word_count[word.split()[0]] = int(word.split()[1])
        return word_count

    def initialize_bigram_count(self):
        bigram_count = {}
        with open(BIGRAMS, "rt") as bigrams:
            for bigram in bigrams.read().split('\n'):
                if bigram:
                    bigram_splitted = bigram.split(' ')
                    bigram_count[(bigram_splitted[0], bigram_splitted[1])] = int(bigram_splitted[2])
        return bigram_count

    def count_sentence_probability(self, sentence):
        ''' Laskee lauseelle todennäköisyyden perustuen siinä esiintyvien
        sanojen ja sanaparien yleisyyteen.

        Parametrit:
        sentence: lause (lista sanoja) jolle todennäköisyys lasketaan
        '''
        result = 0
        for i in range(0, len(sentence) - 1):
            bigram_count = self._bigram_count[(sentence[i], sentence[i + 1])]\
                if (sentence[i], sentence[i + 1]) in self._bigram_count else 0
            word_count = self._word_count[sentence[i]] if sentence[i] in self._word_count else 0
            result += bigram_count/(self._total_words + word_count) + word_count/self._total_words
        return result
