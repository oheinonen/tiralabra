from levenshtein import Levenshtein
from dictionary import TrieNode
from console_io import ConsoleIO

WORDS = "./words.txt"

def main():
    print('Alustetaan sanastoa...')
    dictionary = TrieNode()
    io = ConsoleIO()
    word_count = {}
    # insert words from file into a trie and add occurences to word_count dict
    for word in open(WORDS, "rt").read().split('\n'):
        if word:
            word_count[word.split()[0].lower()] = int(word.split()[1])
            dictionary.insert( word.split()[0].lower() )

    print('Sanasto alustettu')
    
    calculator = Levenshtein(dictionary, io)
    word = io.read('Sana: \n')

    while(word):
        results_1_edit = calculator.search(word, 1)
        results_2_edit = calculator.search(word, 2)
        results = set(results_1_edit + results_2_edit)
        candidates = sort_by_counts(results, word_count)
        io.write('10 käytetyintä:')
        for candidate in candidates:
            io.write(f'{candidate[0]}, {candidate[1]}')
        word = io.read('Uusi sana (poistu tyhjällä syötteellä): \n')
    io.write('hei hei')

def sort_by_counts(candidates, word_count):
    sorted_candidates = []
    for candidate in sorted(candidates, key=lambda x: word_count[x], reverse=True):
        sorted_candidates.append((candidate,word_count[candidate]))
    return sorted_candidates[:10]


if __name__ == "__main__":
    main()