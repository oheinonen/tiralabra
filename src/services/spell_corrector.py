import itertools
MAX_TYPOS_IN_WORD = 1
MAX_TYPOS_IN_SENTENCE = 2

class SpellCorrector():
    '''Luokka ohjelman päätoiminnoille'''
    def __init__(self, calculator, dictionary):
        ''' Luokan konstruktori

        Parametrit:
        calculator: Levenshtein-etäsyyden laskemiseen käytettävä luokka
        dictionary: Sanastoa ylläpitävä ja käyttävä luokka
        '''
        self._calculator = calculator
        self._dictionary = dictionary

    def fix_sentence(self, input_sentence):
        ''' Oikeinkirjoituskorjaajan pääfunktio. Saa käyttäjältä tarkastettavan lauseen,
        ja esittää mahdollisia korjauksia hyödyntäen luokan muita metodeja.
        '''
        candidates = self.get_candidates_for_words(input_sentence)
        # Muodostaa sanoista kaikki mahdolliset permutaatiot (= 'korjatut' lauseet)
        candidate_sentences = list(itertools.product(*candidates))
        probabilities = self.get_sentence_probabilities(candidate_sentences, input_sentence)
        sentences_with_max_typos = filter(lambda x: x[1] <= MAX_TYPOS_IN_SENTENCE, probabilities)
        # Näytetään käyttäjälle viisi todennäköisinta lausetta
        return sorted(sentences_with_max_typos, key=lambda x: x[0], reverse=True)[:5]

    def get_candidates_for_words(self, list_of_words):
        ''' Muodostaa kullekin sanalistan sanalle listan vaihtoehtoisia sanoja,
        jotka ovat sanastossa ja joissa typojen määrä <= MAX_TYPOS_IN_WORD

        Parametrit:
        list_of_words: lista sanoja joille vaihtoehdot haetaan
        '''
        candidates = []
        for word in list_of_words:
            candidates.append([word])
            if not self._dictionary.search(word):
                one_edit_words = self._calculator.search(word, MAX_TYPOS_IN_WORD)
                candidates [-1] += one_edit_words
        return candidates

    def get_sentence_probabilities(self, sentences, original_sentence):
        ''' Laskee annetuille lauseille niiden todennäköisyyden ja typojen määrän hyödyntäen
        metodeja

        Parametrit:
        sentences: liszta lauseita (lause = lista sanoja))
        original_sentence: alkuperäinen käyttäjän antama lause
        '''
        results = []
        for sentence in sentences:
            score = self._dictionary.count_sentence_probability(sentence)
            nof_changes = self.count_changes_in_sentence(sentence, original_sentence)
            results.append((score, nof_changes, sentence))
        return results

    def count_changes_in_sentence(self, sentence1, sentence2):
        ''' Laskee kahden lauseen väliset erot.'''
        result = 0
        for (i, _) in enumerate(sentence1):
            if not sentence1[i] == sentence2[i]:
                result += 1
        return result

