class Ui():
    '''Luokka ohjelman päätoiminnoille'''
    def __init__(self, console_io, service):
        ''' Luokan konstruktori

        Parametrit:
        console_io: lukemiseen ja tulostamiseen käytettävä luokka
        service: oikenkirjoituksen tarkastamiseen käytettävä palvelu
        '''
        self._console_io = console_io
        self._service = service

    def run(self):
        ''' Oikeinkirjoituskorjaajan pääfunktio. Saa käyttäjältä tarkastettavan lauseen,
        ja esittää parhaat korjausehdotukset käyttäjälle.
        '''
        self.print_preface()
        input_sentence = self._console_io\
            .read('Syötä lause jonka oikeikirjoituksen haluat tarkastaa: \n').split(' ')
        while input_sentence[0]:
            results = self._service.fix_sentence(list( map(lambda x: x.lower(), input_sentence) ) )
            self.show_results(input_sentence, results)
            input_sentence = self._console_io.read('Uusi lause (poistu tyhjällä syötteellä): \n')\
                .split(' ')
        self._console_io.write('hei hei')
    
    def show_results(self, input_sentence, results):
            correct = ''
            for result in results:
                candidate = []
                for i in range(len(result[2])):
                    if input_sentence[i].istitle():
                        candidate.append(result[2][i].title())
                    else:
                        candidate.append(result[2][i])
                candidate = self.tuple_to_string(candidate)
                correct = self._console_io.read(f'Tarkoititko "{candidate}" (y/n)?\n')
                if correct == 'y':
                    self._console_io.write(f'Lauseen oikea kirjoitusmuoto "{candidate}"')
                    break
            if correct != 'y':
                self._console_io.write('Lausetta ei löytynyt')

    def print_preface(self):
        self._console_io\
            .write('Tällä ohjelmalla voit tarkastaa englanninkielisen lauseen kirjoitusmuodon.')
        self._console_io\
            .write('Ohjelma ehdottaa lauseelle 1-5 korjattua lausetta.')
        self._console_io\
            .write('Hyväksy korjausehdotus syöttämällä "y" (yes).')
        self._console_io\
            .write('Hylkää ja näytä seuraava ehdotus syöttämällä "n" (no).')
        self._console_io\
            .write('Tämän jälkeen voit halutessasi antaa uuden lauseen tai poistua ohjelmasta tyhjällä syötteellä.\n')

    def tuple_to_string(self, tup):
        '''Muodostaa listamuotoisesta lauseesta merkkijonon'''
        sentence = ''
        for item in tup:
            sentence += item + ' '
        return sentence[:-1]
