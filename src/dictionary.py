''' Moduuli trie-tietorakenteen ylläpitoon'''
class TrieNode:
    ''' Trienode luokkaa käytetään sanojen tallettamiseen.
    Kirjaimet ovat solmuja, ja niiden lapset seuraavia mahdollisia
    kirjaimia sanassa. Jos solmu on jonkin sanan viimeinen kirjain,
    talletetaan tieto solmuun.
    '''
    def __init__(self):
        '''Luokan konstruktori'''
        self.word = None
        self.children = {}

    def insert( self, word ):
        '''Funktio sanan lisäämiseen sanastoon. Lisää sanan tietorakenteeseen
        kirjain kerrallaan ja luo tarvittaessa uusia solmuja'''
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]

        node.word = word
