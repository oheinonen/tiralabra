import unittest
from entities.levenshtein import Levenshtein
from dictionary import Dictionary

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
        self.dictionary = Dictionary()
        self.io = StubIO([self.test_word])
        self.calculator = Levenshtein(self.dictionary)
    
    def test_search_returns_correct_word_with_one_added_letter(self):
        self.assertEqual(self.calculator.search('softwaree',1)[0], 'software')

    def test_search_returns_correct_word_with_one_removed_letter(self):
        self.assertEqual(self.calculator.search('softwre',1)[0], 'software')

    def test_search_returns_correct_word_with_one_switched_letter(self):
        self.assertEqual(self.calculator.search('softwere',1)[0], 'software')

    def test_search_returns_correct_word_with_two_letters_switched(self):
        self.assertEqual(self.calculator.search('softwrae',1)[0], 'software')

    def test_search_returns_correct_words_one_edit(self):
        results = self.calculator.search('humle', 1)
        self.assertEqual(len(results), 2)
        self.assertListEqual(results, ['humble', 'hume'])

    def test_search_returns_correct_words_two_edits(self):
        results = self.calculator.search('humle', 2)
        self.assertEqual(len(results), 70)