## Yksikkötestaus
Yksikkötestauksen kattavuusraportti näkyvillä [täällä](https://app.codecov.io/gh/oheinonen/tiralabra).

Yksikkötestit voidaan toistaa komennolla `poetry run pytest`
### Sanasto
Testauksessa tarkistetaan, että todennäköisyys lauseen oikeinkirjoitukselle on nolla, mikäli mikään lauseen sanoista ei löydy sanastosta. Lisäksi testataan, että lauseen todennäköisyys on jotain väliltä 0...1, kun lauseen sanat ovat sanastossa.

### Trie-tietorakenne
Testauksessa varmistetaan että sanastoon lisätty sana löytyy myöhemmin sanastosta.

### Levenshtein etäisyyden laskija
Testauksessa varmistetaan että luokan hakufunktio palauttaa kaikki sanat annetulla Levenshtein etäisyydellä syötesanasta.

### Spell Corrector / pääohjelma
Testit varmistavat, että 
- ohjelman metodi `count_changes_in_sentence` laskee lauseen muutokset syötteenä annettuun lauseeseen oikein
- sanaston metodia `get_sentence_probabilities` kutsutaan oikeilla arvoilla
- ohjelma toimii syötteellä, jossa lauseelle löytyy oikea korjausehdotus
- ohjelma toimii syötteellä, kun lauseelle ei löydy yhtään korjausehdotusta
