import itertools
from dictionary import initialize_word_count,initialize_bigram_count
MAX_TYPOS_IN_WORD = 1
MAX_TYPOS_IN_SENTENCE = 2

class SpellCorrector():
    def __init__(self, io, calculator):
        ''' Luokan konstruktori

        Parametrit:
        io: lukemiseen ja tulostamiseen käytettävä luokka
        calculator: Levenshtein-etäsyyden laskemiseen käytettävä luokka
        '''
        self._io = io
        self._calculator = calculator
        # Hakemistot sekä yksittäisten sanojen että sanaparien yleisyyden saamiseksi
        self._word_count = initialize_word_count()
        self._bigram_count = initialize_bigram_count()
        self._total_words = sum(self._word_count.values())

    def run(self):
        ''' Oikeinkirjoituskorjaajan pääfunktio. Saa käyttäjältä tarkastettavan lauseen,
        ja esittää mahdollisia korjauksia hyödyntäen luokan muita metodeja.
        '''
        input_sentence = self._io.read('Syötä lause jonka oikeikirjoituksen haluat tarkastaa: \n') \
            .split(' ')
        while(input_sentence[0]):
            candidates = self.get_candidates_for_words(input_sentence)
            # muodosta sanoista kaikki mahdolliset permutaatiot (= 'korjatut' lauseet)
            candidate_sentences = list(itertools.product(*candidates))
            probabilities = self.get_sentence_probabilities(candidate_sentences, input_sentence)
            # Näytetään käyttäjälle 10 todennäköisinta sanaa
            correct = ''
            for result in sorted(filter(lambda x: x[1] <= MAX_TYPOS_IN_SENTENCE, probabilities),
                key=lambda x: x[0], reverse=True)[:10]:
                correct = self._io.read(f'Tarkoititko "{result[2]}" (y/n)? \n')
                if correct == 'y':
                    break
            if correct != 'y':
                self._io.write('Lausetta ei löytynyt')
            input_sentence = self._io.read('Uusi lause (poistu tyhjällä syötteellä): \n').split(' ')
        self._io.write('hei hei')

    def get_candidates_for_words(self, list_of_words):
        ''' Muodostaa kullekin sanalistan sanalle listan vaihtoehtoisia sanoja,
        jotka ovat sanastossa ja joissa typojen määrä <= MAX_TYPOS_IN_WORD

        Parametrit:
        list_of_words: lista sanoja joille vaihtoehdot haetaan
        '''
        candidates = []
        for word in list_of_words:
            one_edit_words = self._calculator.search(word, MAX_TYPOS_IN_WORD)
            candidates.append(one_edit_words)
        return candidates

    def get_sentence_probabilities(self, sentences, original_sentence):
        ''' Laskee annetuille lauseille niiden todennäköisyyden ja typojen määrän hyödyntäen
        luokan muita metodeja

        Parametrit:
        sentences: lista lauseita (lause = lista sanoja))
        original_sentence: alkuperäinen käyttäjän antama lause
        '''
        results = []
        for sentence in sentences:
            score = self.count_sentence_probability(sentence)
            nof_changes = self.count_changes_in_sentence(sentence, original_sentence)
            results.append((score, nof_changes, self.tuple_to_string(sentence)))
        return results

    def count_sentence_probability(self, sentence):
        ''' Laskee lauseelle todennäköisyyden perustuen siinä esiintyvien
        sanojen ja sanaparien yleisyyteen.

        Parametrit:
        sentence: lause (lista sanoja) jolle todennäköisyys lasketaan
        '''
        result = 0
        for i in range(0, len(sentence) - 1):
            bigram_count = self._bigram_count[(sentence[i], sentence[i + 1])]\
                if (sentence[i], sentence[i + 1]) in self._bigram_count else 0
            word_count = self._word_count[sentence[i]] if sentence[i] in self._word_count else 1
            result += bigram_count/(self._total_words + word_count) + word_count/self._total_words
        return result

    def count_changes_in_sentence(self, sentence1, sentence2):
        ''' Laskee kahden lauseen väliset erot.'''
        result = 0
        for (i, word) in enumerate(sentence1):
            if not sentence1[i] == sentence2[i]:
                result += 1
        return result

    def tuple_to_string(self, tup):
        '''Muodostaa listamuotoisesta lauseesta string muotoisen'''
        sentence = ''
        for item in tup:
            sentence += item + ' '
        return sentence[:-1]
