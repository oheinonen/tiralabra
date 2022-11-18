## Yksikkötestaus
Yksikkötestauksen kattavuusraportti näkyvillä [täällä](https://app.codecov.io/gh/oheinonen/tiralabra).

Yksikkötestit voidaan toistaa komennolla `poetry run pytest`
### Sanaston Trie-tietorakenne
Testauksessa varmistetaan että sanastoon lisätty sana löytyy myöhemmin sanastosta.
### Levenshtein etäisyyden laskija
Testauksessa varmistetaan että luokan hakufunktio palauttaa kaikki sanat annetulla Levenshtein etäisyydellä syötesanasta.
