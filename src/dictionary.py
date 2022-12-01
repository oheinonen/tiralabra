from trienode import TrieNode

WORDS = "./frequency_dictionary_en_82_765.txt"
BIGRAMS = "./frequency_bigramdictionary_en_243_342.txt"

class Dictionary:
    ''' Luokka sanaston alustamiseen ja käyttämiseen '''
    def __init__(self):
        self._root = self.initialize_dictionary()
        self._word_counts = self.initialize_word_counts()
        self._bigram_counts = self.initialize_bigram_counts()
        self._total_words = sum(self._word_counts.values())

    def initialize_dictionary(self):
        ''' Alustaa sanaston trienode-luokan avulla'''
        initial_node = TrieNode()
        with open(WORDS, "rt", encoding="utf-8") as words:
            for word in words.read().split('\n'):
                initial_node.insert( word.split()[0] )
        return initial_node

    def initialize_word_counts(self):
        '''Alustaa hakemiston, josta voidaan hakea sanaston sanoille niiden yleisyys'''
        word_count = {}
        with open(WORDS, "rt", encoding="utf-8") as words:
            for word in words.read().split('\n'):
                word_count[word.split()[0]] = int(word.split()[1])
        return word_count

    def initialize_bigram_counts(self):
        '''Alustaa hakemiston, josta voidaan hakea sanaston sanapareille niiden yleisyys'''
        bigram_count = {}
        with open(BIGRAMS, "rt", encoding="utf-8") as bigrams:
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
            bigram = (sentence[i], sentence[i + 1])
            word = sentence[i]
            bigram_count = self._bigram_counts[bigram] if bigram in self._bigram_counts else 0
            word_count = self._word_counts[word] if word in self._word_counts else 0
            bigram_probability = bigram_count/(self._total_words + word_count)
            word_probability = word_count/self._total_words
            result +=  bigram_probability + word_probability
        return result
