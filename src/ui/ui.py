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
        input_sentence = self._console_io\
            .read('Syötä lause jonka oikeikirjoituksen haluat tarkastaa: \n').split(' ')
        while input_sentence[0]:
            results = self._service.fix_sentence(input_sentence)
            correct = ''
            for result in results:
                correct = self._console_io.read(f'Tarkoititko "{result[2]}" (y/n)?\n')
                if correct == 'y':
                    self._console_io.write(f'Lauseen oikea kirjoitusmuoto "{result[2]}"')
                    break
            if correct != 'y':
                self._console_io.write('Lausetta ei löytynyt')
            input_sentence = self._console_io.read('Uusi lause (poistu tyhjällä syötteellä): \n')\
                .split(' ')
        self._console_io.write('hei hei')
