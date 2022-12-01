import unittest
from trienode import TrieNode

class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.word = 'testword'
        self.initial_word = 'initialWord'
        self.trienode = TrieNode()
        self.trienode.insert(self.initial_word)

    def test_search_returns_word_if_in_trienode(self):
        self.trienode.search(self.initial_word)
        self.assertEqual(self.initial_word, self.trienode.search(self.initial_word))

    def test_search_returns_none_if_not_in_trienode(self):
        self.assertIsNone(self.trienode.search(self.word))

    def test_added_word_is_in_trienode(self):
        self.trienode.insert(self.word)
        self.assertEqual(self.word, self.trienode.search(self.word))