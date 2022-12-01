import unittest
from dictionary import Dictionary
from unittest.mock import Mock, ANY

class TestDictionary(unittest.TestCase):
    def setUp(self):
        self.dictionary = Dictionary()

    def test_sentence_probability_is_zero_when_words_are_not_in_dictionary(self):
        probability = self.dictionary.count_sentence_probability('sanat eivat sanastossa'.split(' '))
        self.assertEqual(probability, 0)
    
    def test_sentence_probability_is_between_zero_and_one_if_at_least_one_word_is_in_dictionary(self):
        probability = self.dictionary.count_sentence_probability('these words exist'.split(' '))
        self.assertTrue(0 <= probability, probability <= 1)
