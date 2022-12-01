'''Moduuli Levenshtein -luokan ylläpitoon'''
class Levenshtein:
    ''' Luokan avulla lasketaan Levenshteinin etäisyys syötteenä
    saadun sanan sekä trie-tietorakeenteen sanojen välille
    '''
    def __init__(self, dictionary):
        ''' Luokan konstruktori joka saa parametrikseen käytetyn sanaston'''
        self._dictionary = dictionary._root


    def search(self, word, max_cost ):
        '''Hakufunktio palauttaa listan pareja, jotka sisältävät jokaisen
        sanaston sanan jonka Levenshtein etäisyys on korkeintaan parametrina
        max_cost annettu kynnysarvo'''

        # alustaa Levenshteinin matriisin
        current_row = range( len(word) + 1 )

        results = []

        # laskee rekursiivisesti etäisyyden jokaiselle sanaston sanalle
        for letter in self._dictionary.children:
            self.search_recursive( self._dictionary.children[letter], letter,'', word, current_row,
            results, max_cost)

        return results

    def search_recursive(
            self, node, letter, previous_letter, word, previous_row, results, max_cost):
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

            if word[column - 2] == letter and word[column - 1] == previous_letter:
                transpose_cost = previous_row[ column - 1 ]
            else:
                transpose_cost = previous_row[ column - 1 ] + 1

            current_row.append( min( insert_cost, delete_cost, replace_cost, transpose_cost) )

        # jos kyseinen solmu on sana ja rivin viimeinen sarake (joka kuvastaa muutosten määrää)
        # arvoltaan kynnysarvoa pienempi, se talletetaan
        if current_row[-1] <= max_cost and node.word is not None:
            results.append(node.word)

        # rekursiivista hakua jatketaan solmun lapsille, jotta saadaan kaikkien
        # sanojen etäisyys laskettua. hakua ei jatketa jos kynnysarvo on ylittynyt
        if min( current_row ) <= max_cost:
            for next_letter in node.children:
                self.search_recursive( node.children[next_letter], next_letter, letter,
                    word, current_row, results, max_cost )
