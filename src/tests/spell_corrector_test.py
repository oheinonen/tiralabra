import unittest
from spell_corrector import SpellCorrector
from dictionary import Dictionary
from unittest.mock import Mock, ANY

class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def read(self, text):
        return self.inputs.pop(0)

    def write(self, text):
        self.outputs.append(text)
    
class TestSpellCorrector(unittest.TestCase):
    def setUp(self):
        self._io = StubIO([])
        self._dictionary = Dictionary()
        self._calculator_mock = Mock()
        self._spellcorrector = SpellCorrector(self._io, self._calculator_mock, self._dictionary)

    def test_changes_in_sentence_is_zero_if_there_are_no_different_words(self):
        sentence = 'Here is no typos'.split(' ')
        nof_changes = self._spellcorrector.count_changes_in_sentence(sentence, sentence)
        self.assertEqual(nof_changes,0)

    def test_changes_in_sentence_is_two_if_there_are_exactly_two_different_words(self):
        sentence1 = 'Here is two typos'.split(' ')
        sentence2 = 'Hre is two typs'.split(' ')
        nof_changes = self._spellcorrector.count_changes_in_sentence(sentence1, sentence2)
        self.assertEqual(nof_changes,2)
    
    def test_candidates_for_words_searched(self):
        sentence = 'Findign candidats'.split(' ')
        self._spellcorrector.get_candidates_for_words(sentence)
        self._calculator_mock.search.assert_called_with('candidats', ANY)

