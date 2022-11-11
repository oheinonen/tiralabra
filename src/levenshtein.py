'''Moduuli Levenshtein -luokan ylläpitoon'''
class Levenshtein:
    ''' Luokan avulla lasketaan Levenshteinin etäisyys syötteenä
    saadun sanan sekä trie-tietorakeenteen sanojen välille
    '''
    def __init__(self, dictionary):
        ''' Luokan konstruktori joka saa parametrikseen käytetyn sanaston'''
        self.dictionary = dictionary

    def execute(self):
        ''' Pääfunktio, joka saa käyttäjältä syötteen,
        määrittää lähimmät vaihtoehdot ja tulostaa ne käyttäjälle.'''
        word = input('Sana: \n')
        results = self.search(word)
        results.sort(key=lambda tuple: tuple[1])
        print('Sanastossa kolme lähintä sanaa:')
        for num in range(3):
            print(f'{results[num][0]}: Levenshtein etäisyys { results[num][1]}')

    def search(self, word ):
        '''Hakufunktio palauttaa listan pareja, jotka sisältävät jokaisen
        sanaston sanan sekä tämän Levenshtein-etäisyyden haettuun sanaan'''

        # alustaa Levenshteinin matriisin
        current_row = range( len(word) + 1 )

        results = []

        # laskee rekursiivisesti etäisyyden jokaiselle sanaston sanalle
        for letter in self.dictionary.children:
            self.search_recursive( self.dictionary.children[letter], letter, word, current_row,
            results )

        # tulokset järjestetään etäisyyden mukaan
        results.sort(key=lambda x: x[1])
        return results

    def search_recursive(self, node, letter, word, previous_row, results ):
        '''Rekursiivinen apufunktio haun toteutukselle'''
        columns = len( word ) + 1
        # Levenshtein etäisyys ensimmäisessä kolumnissa on aina yhtä kuin
        # rivien määrä (eli kyseisellä hetkellä tarkasteltavan osamerkkijonon pituus)
        current_row = [ previous_row[0] + 1 ]

        # muodostaa uuden rivin käsiteltävän kirjaimen mukaan. sarakkeiden arvot
        # vastaavat tarkasteltavan ja tavoitesanan osamerkkijonojen Levenshtein etäisyyttä
        for column in range( 1, columns ):

            insert_cost = current_row[column - 1] + 1
            delete_cost = previous_row[column] + 1

            if word[column - 1] != letter:
                replace_cost = previous_row[ column - 1 ] + 1
            else:
                replace_cost = previous_row[ column - 1 ]

            current_row.append( min( insert_cost, delete_cost, replace_cost ) )

        # jos kyseinen solmu on sana, se talletetaan
        if node.word is not None:
            results.append( (node.word, current_row[-1] ) )

        # rekursiivista hakua jatketaan solmun lapsille, jotta saadaan kaikkien
        # sanojen etäisyys laskettua
        for next_letter in node.children:
            self.search_recursive( node.children[next_letter], next_letter, word, current_row,
                results )
