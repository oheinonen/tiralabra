import unittest
from unittest.mock import Mock, ANY
from ui.ui import Ui
from services.spell_corrector import SpellCorrector
from dictionary import Dictionary
from entities.levenshtein import Levenshtein

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
        self._dictionary = Dictionary()
        self._calculator = Levenshtein(self._dictionary)
        self._spellcorrector = SpellCorrector(self._calculator, self._dictionary)

    def test_changes_in_sentence_is_zero_if_there_are_no_different_words(self):
        sentence = 'Here is no typos'.split(' ')
        nof_changes = self._spellcorrector.count_changes_in_sentence(sentence, sentence)
        self.assertEqual(nof_changes,0)

    def test_changes_in_sentence_is_two_if_there_are_exactly_two_different_words(self):
        sentence1 = 'Here is two typos'.split(' ')
        sentence2 = 'Hre is two typs'.split(' ')
        nof_changes = self._spellcorrector.count_changes_in_sentence(sentence1, sentence2)
        self.assertEqual(nof_changes,2)
    
    def test_word_is_checked_from_dictionary(self):
        dictionary_mock = Mock()
        calculator = Levenshtein(dictionary_mock)
        spellcorrector = SpellCorrector(calculator, dictionary_mock)
        sentence = 'Findign candidats'.split(' ')
        spellcorrector.get_candidates_for_words(sentence)
        dictionary_mock.search.assert_called_with('candidats')
    
    def test_candidates_for_words_are_searched(self):
        calculator_mock = Mock()
        spellcorrector = SpellCorrector(calculator_mock, self._dictionary)
        sentence = 'Findign candidats'.split(' ')
        calculator_mock.search.return_value = ['candidats']
        spellcorrector.get_candidates_for_words(sentence)
        calculator_mock.search.assert_called_with('candidats', ANY)

    def test_sentence_probabilities_searched(self):
        dictionary_mock = Mock()
        calculator = Levenshtein(dictionary_mock)
        spellcorrector = SpellCorrector(calculator, dictionary_mock)
        sentences = ['Probabilities searched'.split(' ')]
        spellcorrector.get_sentence_probabilities(sentences, sentences[0])
        dictionary_mock.count_sentence_probability.assert_called_with(sentences[0])

    def test_spell_corrector_with_good_input(self):
        io = StubIO(['good morning', 'y', ''])
        dictionary = Dictionary()
        calculator = Levenshtein(dictionary)
        spellcorrector = SpellCorrector(calculator, dictionary)
        ui = Ui(io, spellcorrector)
        ui.run()
        self.assertTrue('Valitsit lauseen oikeaksi kirjoitusmuodoksi: "good morning"\n' in io.outputs)
    
    def test_spell_corrector_with_sentence_having_zero_matches(self):
        io = StubIO(['dfasdfas asdfasdfa','y', ''])
        dictionary = Dictionary()
        calculator = Levenshtein(dictionary)
        spellcorrector = SpellCorrector(calculator, dictionary)
        ui = Ui(io, spellcorrector)
        ui.run()
        self.assertTrue('Valitsit lauseen oikeaksi kirjoitusmuodoksi: "dfasdfas asdfasdfa"\n'  in io.outputs)