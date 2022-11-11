from levenshtein import Levenshtein
from dictionary import TrieNode

def main():
    dictionary = TrieNode()
    for word in ['testi', 'sanasto', 'tässä', 'hei']:
        dictionary.insert( word )

    calculator = Levenshtein(dictionary)
    calculator.execute()

if __name__ == "__main__":
    main()
