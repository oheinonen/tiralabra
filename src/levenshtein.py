class Levenshtein:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def execute(self):
        word = input('Sana: \n')
        results = self.search(word)
        results.sort(key=lambda x: x[1])
        print(f'Sanastossa kolme lähintä sanaa:')
        for x in range(3):
            print(f'{results[x][0]}: Levenshtein etäisyys { results[x][1]}')

    # hakufunktio palauttaa listan pareja, jotka sisältävät jokaisen sanaston sanan sekä tämän Levenshtein-etäisyyden haettuun sanaan
    def search(self, word ):
        # alustaa Levenshteinin matriisin
        currentRow = range( len(word) + 1 )

        results = []

        # laskee rekursiivisesti etäisyyden jokaiselle sanaston sanalle
        for letter in self.dictionary.children:
            self.searchRecursive( self.dictionary.children[letter], letter, word, currentRow, results )
        
        # tulokset järjestetään etäisyyden mukaan
        results.sort(key=lambda x: x[1])
        return results

    # rekursiivinen apufunktio haun toteutukselle
    def searchRecursive(self, node, letter, word, previousRow, results ):

        columns = len( word ) + 1
        # Levenshtein etäisyys ensimmäisessä kolumnissa on aina yhtä kuin rivien määrä (eli kyseisellä hetkellä tarkasteltavan osamerkkijonon pituus)
        currentRow = [ previousRow[0] + 1 ]

        # muodostaa uuden rivin käsiteltävän kirjaimen mukaan. sarakkeiden arvot vastaavat tarkasteltavan ja tavoitesanan osamerkkijonojen Levenshtein etäisyyttä
        for column in range( 1, columns ):

            insertCost = currentRow[column - 1] + 1
            deleteCost = previousRow[column] + 1

            if word[column - 1] != letter:
                replaceCost = previousRow[ column - 1 ] + 1
            else:                
                replaceCost = previousRow[ column - 1 ]

            currentRow.append( min( insertCost, deleteCost, replaceCost ) )

        # jos kyseinen solmu on sana, se talletetaan 
        if node.word != None:
            results.append( (node.word, currentRow[-1] ) )

        # rekursiivista hakua jatketaan solmun lapsille, jotta saadaan kaikkien sanojen etäisyys laskettua
        for letter in node.children:
            self.searchRecursive( node.children[letter], letter, word, currentRow, 
                results )


