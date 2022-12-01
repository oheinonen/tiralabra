from levenshtein import Levenshtein
from dictionary import Dictionary
from console_io import ConsoleIO
from spell_corrector import SpellCorrector

def main():
    io = ConsoleIO()
    io.write('Alustetaan sanastoa...')
    dictionary = Dictionary()
    io.write('Sanasto alustettu')
    calculator = Levenshtein(dictionary)
    spell_corrector = SpellCorrector(io, calculator, dictionary)
    spell_corrector.run()

if __name__ == "__main__":
    main()
