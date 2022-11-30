import itertools
from dictionary import initialize_word_count,initialize_bigram_count

class SpellCorrector():
    def __init__(self, io, calculator):
        self._io = io
        self._calculator = calculator
        self._word_count = initialize_word_count()
        self._bigram_count = initialize_bigram_count()
        self._total_words = sum(self._word_count.values())

    def run(self):
        input_sentence = self._io.read('Syötä lause jonka oikeikirjoituksen haluat tarkastaa: \n').split(' ')
        while(input_sentence[0]):
            # Jokaiselle lauseen sanalle haetaan sanastosta lista sanoja, jotka ovat yhden typon päässä 
            candidates = self.get_candidates_for_words(input_sentence)

            # Muodostetaan sanoista kaikki mahdolliset permutaatiot  
            candidate_sentences = list(itertools.product(*candidates))

            # Lasketaan jokaiselle mahdolliselle lauseelle todennäköisyys perustuen käytettyjen sanojen sekä peräkkäisten sanojen yleisyyteen
            probabilities = self.get_sentence_probabilities(candidate_sentences, input_sentence)
            
            # Näytetään käyttäjälle 10 todennäköisinta sanaa, joissa on max kaksi sanaa yhdellä typolla
            correct = ''
            for result in sorted(filter(lambda x: x[1] < 3, probabilities), key=lambda x: x[0], reverse=True)[:10]:
                correct = self._io.read(f'Tarkoititko "{result[2]}" (y/n)? \n')
                if correct == 'y':
                    break
            if correct != 'y':
                self._io.write('Lausetta ei löytynyt')
            input_sentence = self._io.read('Uusi lause (poistu tyhjällä syötteellä): \n').split(' ')
        self._io.write('hei hei')

    def get_candidates_for_words(self, list_of_words):
        candidates = []
        for word in list_of_words :
            one_edit_words = self._calculator.search(word, 1)
            candidates.append(one_edit_words)
        return candidates
    
    def get_sentence_probabilities(self, sentences,original_sentence):
        results = []
        for sentence in sentences:
            score = self.count_sentence_probability(sentence, self._word_count, self._bigram_count, self._total_words)
            nof_changes = self.count_changes_in_sentence(sentence, original_sentence)
            results.append((score, nof_changes, self.tuple_to_string(sentence)))
        return results

    def count_sentence_probability(self, sentence, word_count, bigram_count, total_words):
        result = 0
        for i in range(0, len(sentence) - 1):
            p3 = bigram_count[(sentence[i], sentence[i + 1])] if (sentence[i], sentence[i + 1]) in bigram_count else 0
            p4 = word_count[sentence[i]] if sentence[i] in word_count else 1
            result += p3/(total_words + p4) + p4/total_words
        return result

    def count_changes_in_sentence(self, candidate_sentence, input_sentence):
        result = len([word for word in candidate_sentence if word not in input_sentence])
        return result

    def tuple_to_string(self, tup):
        str = ''
        for item in tup:
            str = str + item + ' '
        return str
