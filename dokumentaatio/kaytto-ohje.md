# Käyttöohje
### Alkutoimet
1. Asenna riippuvuuksien hallintaan käytettävä Poetry-työkalu [täältä löytyvien ohjeiden avulla](https://python-poetry.org/docs/)
2. Kloonaa repo koneellesi
3. Asenna riippuvuudet komennolla `poetry install`

### Ohjelman käyttäminen
1. Käynnistä ohjelma komennolla `poetry run python3 src/index.py`. Ohjelma toimii terminaalissa. Tuloste on suomea, mutta annettava syöte tulisi olla englantia - ohjelma ei osaa korjata muita kieliä. 

2. Syötä lause, jonka oikeinkirjoituksen haluat tarkastaa. Tämän jälkeen ohjelma esittää lauseelle mahdollisia vaihtoehtoja, kuitenkin maksimissaan kymmenen kappaletta. 
3. Mikäli tarkoittamasi lause ehdotetaan, voit lopettaa vaihtoehtojen esityksen komennolla `y`. 
4. Tämän jälkeen voit antaa uuden lauseen, tai poistua painamalla enteriä.

### Maagisten numeroiden vaihtaminen
Ohjelman `SpellCorrector`-luokassa on kaksi maagista numeroa; `MAX_TYPOS_IN_WORD` (oletus 1) ja `MAX_TYPOS_IN_SENTENCE` (oletus 2). Näitä muokkaamalla käyttäjä voi tehdä ohjelmasta itselleen sopivamman pohjautuen omaan näkemykseen typojen määrästä. Lukujen kasvattaminen hidastaa ohjelman toimivuutta, ja pienikin muutos näissä saattaa tehdä ohjelmasta käyttökelvottoman. Lisää aiheesta testausdokumentissa.
