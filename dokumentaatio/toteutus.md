## Ohjelman yleisrakenne
Ohjelmassa on kuusi luokkaa, `SpellCorrector`,`Dictionary`, `TrieNode`, `Levenshtein`. `Ui` ja `ConsoleIO` . `SpellCorrector`-luokka sisältää metodit jonka perusteella todennäköisimmät korjausehdotukset muodostetaan, `Dictionary` -luokkaa käytetään sanaston ylläpitoon ja käsittelyyn. `TrieNode` -luokkaa hyödynnetään sanaston tietorakenteena. `Levenshtein` -luokka käytetään siihen, että annetulle sanalle voidaan hakea vaihtoehtoiset sanat annetulla virhemarginaalilla. 

``` mermaid
  classDiagram
      class Ui
      class ConsoleIo
      class Dictionary
      class SpellCorrector
      class TrieNode
      class Levenshtein
      Ui  --|>  ConsoleIo
      Ui  --|>  SpellCorrector
      SpellCorrector  --|>  Levenshtein
      SpellCorrector  --|>  Dictionary
      Levenshtein --|> Dictionary
      Dictionary --|> TrieNode
```

`Ui` luokka sisältää ohjelman pääfunktion ja muotoilee tulostuksen. Pääfunktio saa käyttäjältä lauseen tarkastettavaksi ja käyttää `SpellCorrector`-luokkaa saadakseen lauseelle korjausehdotuksia. Saaduista sanalistoista muodostetaan ehdokkaita korjatuksi lauseeksi. Näille lauseille määritetään todennäköisyys laskemalla kunkin sanan todennäköisyys (=yleisyys kielessä), sekä lauseen peräkkäisten sanojen sanaparien yleisyys kielessä. Näitä varten on hyödynnetty [täältä saatua dataa](https://github.com/mammothb/symspellpy).

Lopulta käyttäjälle ehdotetaan max viisi lausetta yksi kerrallaan lauseita todennäköisyyksien mukaan.

### Trie-tietorakenne esimerkki
``` mermaid
  graph TD
      A[ ] --> D
      A --> C
      A --> I
      D --> DO
      D --> DI
      DO --> DOG
      I --> IC
      I --> IT
      A --> ...
```
### Damerau-Levenshtein etäisyys
Erilaiset typot, jotka ohjelma tarkastaa ovat 
1. kirjaimen poisto: _softwaree -> software_
2. kirjaimen lisääminen: _softwre -> software_
3. kirjaimen vaihto: _softwere -> software_
4. kahden kirjaimen vaihto: _softwrae -> software_

Näiden typojen avulla lasketaan sanojen Damerau-Levenshtein etäisyys. 
Esim. sanojen _code_ ja _clown_ etäisyys on 3: __code->clode->clowe->clown__

## Työn mahdolliset puutteet ja parannusehdotukset
Aiheesta löytyy runsaasti kirjallisuutta, joten puutteita ja parannusehdotuksia löytyy paljon. Tässä listattuna muutamia tärkeimpiä parannusehdotuksia:
1. Kontekstin huomioon ottaminen
2. Sanaston laajentaminen
3. Mahdollisten virheiden määrän kasvattaminen
4. Virheen laadun arviointi

### Kontekstin huomioon ottaminen
Tämä lienee tärkein parannus, joka ohjelmaan voitaisiin tehdä. Koska kontekstia ei huomioida, yleisesti käytetyt sanat tulevat useammin suositelluksi kuin harvemmin käytetyt. Kontekstin huomioon ottaminen mahdollistaisi myös ongelman #3 ratkaisemisen, sillä kontekstin avulla voitaisiin filtteröidä iso joukko sanoista pois.

### Sanaston laajentaminen
Tähän kaatuu monet kääntämisyritykset, sillä mikäli sanaa ei löydy sanastosta ei sitä myöskään korjata oikein. 

### Mahdollisten virheiden määrän kasvattaminen
Tällä hetkellä ohjelma toimii liian hitaasti, mikäli sanalle annetaan esimerkiksi kolme typoa. Tämä johtuu siitä, että etenkin lyhyille sanoille löytyy tällöin valtava määrä korjausehdotuksia. 

### Virheen laadun arviointi
Monet kirjoitusvirheet ovat ihmiselle helposti ymmärrettävissä, mutta koneelle vaikeampia. Ohjelman tulisi antaa enemmän painoarvoa esimerkiksi typoille, joissa kirjaimet ovat vierekkäin näppäimistöllä (_foyl_ -> _foul_), kun samaa kirjainta laitetaan yksi liikaa tai liian vähän (_adres_ -> _address_) tai tietyille kirjaimille, jotka saatetaan sekoittaa toisiinsa (_assess_ -> _access_).  

## Lähteet
- [http://norvig.com/spell-correct.html](http://norvig.com/spell-correct.html)
- [http://stevehanov.ca/blog/?id=114](http://stevehanov.ca/blog/?id=114)
- [https://en.wikipedia.org/wiki/Levenshtein_distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [https://en.wikipedia.org/wiki/Levenshtein_automaton](https://en.wikipedia.org/wiki/Levenshtein_automaton)
- [https://wolfgarbe.medium.com/1000x-faster-spelling-correction-algorithm-2012-8701fcd87a5f](https://wolfgarbe.medium.com/1000x-faster-spelling-correction-algorithm-2012-8701fcd87a5f)
- [https://seekstorm.com/blog/pruning-radix-trie/](https://seekstorm.com/blog/pruning-radix-trie/)
- https://github.com/mammothb/symspellpy
- [https://towardsdatascience.com/spelling-correction-how-to-make-an-accurate-and-fast-corrector-dc6d0bcbba5f](https://towardsdatascience.com/spelling-correction-how-to-make-an-accurate-and-fast-corrector-dc6d0bcbba5f)
