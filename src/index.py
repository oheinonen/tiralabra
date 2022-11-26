from levenshtein import Levenshtein
from dictionary import TrieNode
from console_io import ConsoleIO
import itertools

WORDS = "./frequency_dictionary_en_82_765.txt"
BIGRAMS = "./frequency_bigramdictionary_en_243_342.txt"

def main():
    print('Alustetaan sanastoa...')
    dictionary = TrieNode()
    io = ConsoleIO()
    word_count = initialize_dictionary(dictionary)
    print('Sanasto alustettu')
    bigram_count = initialize_bigram_count()
    total_words = sum(word_count.values())
        
    calculator = Levenshtein(dictionary, io)
    input_sentence = io.read('Lause: \n')

    candidates = []
    while(input_sentence):
        input_sentence_list = input_sentence.split(' ')
        # Jokaiselle lauseen sanalle haetaan sanastosta lista sanoja, jotka ovat yhden typon päässä 
        for word in input_sentence_list :
            results_1_edit = calculator.search(word, 1)
            candidates.append(results_1_edit)

        # Muodostetaan sanoista kaikki mahdolliset permutaatiot  
        candidate_sentences = list(itertools.product(*candidates))

        results = []

        # Lasketaan jokaiselle mahdolliselle lauseelle todennäköisyys perustuen käytettyjen sanojen sekä peräkkäisten sanojen yleisyyteen
        for candidate_sentence in candidate_sentences:
            score = count_sentence_probability(candidate_sentence, word_count, bigram_count, total_words)
            # Lasketaan kuinka monta väärinkirjoitettua sanaa lause sisältää
            nof_changes = count_sentence_changes(candidate_sentence, input_sentence_list)
            results.append((score, nof_changes, tuple_to_string(candidate_sentence)))

        correct = 'n'
        while correct != 'y':
            # Näytetään käyttäjälle 10 todennäköisinta sanaa, joissa on max kaksi sanaa yhdellä typolla
            for result in sorted(filter(lambda x: x[1] < 3, results), key=lambda x: x[0], reverse=True)[:10]:
                correct = io.read(f'Tarkoititko "{result[2]}" (y/n)? \n')
            print('Lausetta ei löytynyt')
            correct = 'y'
        input_sentence = io.read('Uusi lause (poistu tyhjällä syötteellä): \n')
    io.write('hei hei')

def initialize_dictionary(dictionary):
    word_count = {}
    for word in open(WORDS, "rt").read().split('\n'):
        word_count[word.split()[0]] = int(word.split()[1])
        dictionary.insert( word.split()[0] )
    return word_count

def initialize_bigram_count():
    bigram_count = {}
    for bigram in open(BIGRAMS, "rt").read().split('\n'):
        if bigram:
            bigram_splitted = bigram.split(' ')
            bigram_count[(bigram_splitted[0], bigram_splitted[1])] = int(bigram_splitted[2])
    return bigram_count


def count_sentence_probability(sentence, word_count, bigram_count, total_words):
    result = 0
    for i in range(0, len(sentence) - 1):
        p3 = bigram_count[(sentence[i], sentence[i + 1])] if (sentence[i], sentence[i + 1]) in bigram_count else 0
        p4 = word_count[sentence[i]] if sentence[i] in word_count else 1
        result += p3/(total_words + p4) + p4/total_words
    return result

def count_sentence_changes(candidate_sentence, input_sentence):
    result = 0
    for i in range(len(candidate_sentence)):
        if not candidate_sentence[i] == input_sentence[i]:
            result += 1
    return result

def tuple_to_string(tup):
    str = ''
    for item in tup:
        str = str + item + ' '
    return str

def list_to_string(s):
    str = ""
    for ele in s:
        str +=  ele + ' '
    return str
 
def sort_by_counts(candidates, word_count):
    sorted_candidates = []
    for candidate in sorted(candidates, key=lambda x: word_count[x], reverse=True):
        sorted_candidates.append((candidate,word_count[candidate]))
    return sorted_candidates[:10]

if __name__ == "__main__":
    main()