import unittest
from levenshtein import Levenshtein
from dictionary import TrieNode
WORDS = "./frequency_dictionary_en_82_765.txt"

class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def read(self, text):
        return self.inputs.pop(0)

    def write(self, text):
        self.outputs.append(text)
    
class TestLevenshtein(unittest.TestCase):
    def setUp(self):
        self.test_word = 'humle'
        self.dictionary = TrieNode()
        self.io = StubIO([self.test_word])
        for word in open(WORDS, "rt").read().split():
                self.dictionary.insert( word.split()[0].lower() )
        self.calculator = Levenshtein(self.dictionary, self.io)

    def test_search_returns_correct_words_one_edit(self):
        results = self.calculator.search(self.test_word, 1)
        self.assertEqual(len(results), 2)
        self.assertListEqual(results, ['humble', 'hume'])

    def test_search_returns_correct_words_two_edits(self):
        results = self.calculator.search(self.test_word, 2)
        self.assertEqual(len(results), 95)