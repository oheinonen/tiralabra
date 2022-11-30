import unittest
from trienode import TrieNode

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.word = 'testword'
        self.initial_word = 'initialWord'
        self.dictionary = TrieNode()
        self.dictionary.insert(self.initial_word)

    def test_search_returns_word_if_in_dictionary(self):
        self.dictionary.search(self.initial_word)
        self.assertEqual(self.initial_word, self.dictionary.search(self.initial_word))

    def test_search_returns_none_if_not_in_dictionary(self):
        self.assertIsNone(self.dictionary.search(self.word))

    def test_added_word_is_in_dictionary(self):
        self.dictionary.insert(self.word)
        self.assertEqual(self.word, self.dictionary.search(self.word))
