from ui.ui import Ui
from ui.console_io import ConsoleIO
from entities.levenshtein import Levenshtein
from dictionary import Dictionary
from services.spell_corrector import SpellCorrector

def main():
    console_io = ConsoleIO()
    console_io.write('Alustetaan sanastoa...')
    dictionary = Dictionary()
    console_io.write('Sanasto alustettu \n')
    calculator = Levenshtein(dictionary)
    spell_corrector = SpellCorrector(calculator, dictionary)
    ui = Ui(console_io, spell_corrector)
    ui.run()

if __name__ == "__main__":
    main()
