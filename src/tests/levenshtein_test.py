import unittest
from levenshtein import Levenshtein


class StubDictionary:
    def __init__(self):
        self.word = None
        self.children = {}

    def insert( self, word ):
        node = self
        for letter in word:
            if letter not in node.children: 
                node.children[letter] = StubDictionary()

            node = node.children[letter]

        node.word = word


class TestLevenshtein(unittest.TestCase):

    def test_calculates_distance_correctly(self):
        dictionary = StubDictionary()
        for word in ['testi', 'sanasto', 'tässä', 'hei']:
            dictionary.insert( word )

        calculator = Levenshtein(dictionary)
        res = calculator.search('sana')
        self.assertEqual(res[0][0], 'sanasto')
        self.assertEqual(res[0][1], 3)
