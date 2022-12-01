import unittest
from spell_corrector import SpellCorrector
from dictionary import Dictionary
from levenshtein import Levenshtein
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
        self._dictionary_mock = Mock()
        self._calculator_mock = Mock()
        self._spellcorrector_mock = SpellCorrector(self._io, self._calculator_mock, self._dictionary_mock)

    def test_changes_in_sentence_is_zero_if_there_are_no_different_words(self):
        sentence = 'Here is no typos'.split(' ')
        nof_changes = self._spellcorrector_mock.count_changes_in_sentence(sentence, sentence)
        self.assertEqual(nof_changes,0)

    def test_changes_in_sentence_is_two_if_there_are_exactly_two_different_words(self):
        sentence1 = 'Here is two typos'.split(' ')
        sentence2 = 'Hre is two typs'.split(' ')
        nof_changes = self._spellcorrector_mock.count_changes_in_sentence(sentence1, sentence2)
        self.assertEqual(nof_changes,2)
    
    def test_candidates_for_words_searched(self):
        sentence = 'Findign candidats'.split(' ')
        self._spellcorrector_mock.get_candidates_for_words(sentence)
        self._calculator_mock.search.assert_called_with('candidats', ANY)

    def test_sentence_probabilities_searched(self):
        sentences = ['Probabilities searched'.split(' ')]
        self._spellcorrector_mock.get_sentence_probabilities(sentences, sentences[0])
        self._dictionary_mock.count_sentence_probability.assert_called_with(sentences[0])

    def test_spell_corrector_with_good_input(self):
        io = StubIO(['god morning','n', 'n', 'n', 'n','n', 'n', 'y', ''])
        dictionary = Dictionary()
        calculator = Levenshtein(dictionary)
        spellcorrector = SpellCorrector(io, calculator, dictionary)
        spellcorrector.run()
        self.assertTrue('Lauseen oikea kirjoitusmuoto "good morning"' in io.outputs)
    
    def test_spell_corrector_with_sentence_having_zero_matches(self):
        io = StubIO(['dfasdfas asdfasdfa',''])
        dictionary = Dictionary()
        calculator = Levenshtein(dictionary)
        spellcorrector = SpellCorrector(io, calculator, dictionary)
        spellcorrector.run()
        self.assertTrue('Lausetta ei löytynyt' in io.outputs)