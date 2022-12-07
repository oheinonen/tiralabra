from entities.trienode import TrieNode

WORDS = "./frequency_dictionary_en_82_765.txt"

class Dictionary:
    ''' Luokka sanaston alustamiseen ja käyttämiseen '''
    def __init__(self):
        self._root = self.initialize_dictionary()
        self._word_counts = self.initialize_word_counts()
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


    def count_sentence_probability(self, sentence):
        ''' Laskee lauseelle todennäköisyyden perustuen siinä esiintyvien
        sanojen yleisyyteen.

        Parametrit:
        sentence: lause (lista sanoja) jolle todennäköisyys lasketaan
        '''
        result = 0
        for i in range(0, len(sentence)):
            word = sentence[i]
            word_count = self._word_counts[word] if word in self._word_counts else 0
            word_probability = word_count/self._total_words
            result += word_probability
        return result
    
    def search(self, word):
        return self._root.search(word)
