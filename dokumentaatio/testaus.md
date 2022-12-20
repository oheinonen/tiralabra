## Yksikkötestaus
Yksikkötestauksen kattavuusraportti näkyvillä [täällä](https://app.codecov.io/gh/oheinonen/tiralabra).

Yksikkötestit voidaan toistaa komennolla `poetry run pytest`
### Sanasto
Testauksessa tarkistetaan, että todennäköisyys lauseen oikeinkirjoitukselle on nolla, mikäli mikään lauseen sanoista ei löydy sanastosta. Lisäksi testataan, että lauseen todennäköisyys on jotain väliltä 0...1, kun lauseen sanat ovat sanastossa.

### Trie-tietorakenne
Testauksessa varmistetaan että sanastoon lisätty sana löytyy myöhemmin sanastosta, ja että sanaa joka ei ole sanastossa ei löydy sanastosta.

### Levenshtein etäisyyden laskija
Testauksessa varmistetaan että luokan hakufunktio palauttaa kaikki sanat annetulla Levenshtein etäisyydellä syötesanasta. Lisäksi testauksessa varmistetaan, että haluttu sana löydetään, kun sanasta on 
1. poistettu kirjain
2. lisätty kirjain
3. vaihdettu kirjain
4. vaihdettu kahden vierekkäisen kirjaimen paikkaa.

### Spell Corrector / pääohjelma
Testit varmistavat, että 
- ohjelman metodi `count_changes_in_sentence` laskee lauseen muutokset syötteenä annettuun lauseeseen oikein
- sanaston metodia `get_sentence_probabilities` kutsutaan oikeilla arvoilla
- ohjelma toimii syötteellä, jossa lauseelle löytyy oikea korjausehdotus
- ohjelma toimii syötteellä, kun lauseelle ei löydy yhtään korjausehdotusta

## Suorituskykytestaus
Varsinaisia suorituskykytestejä ohjelmaan ei ole tehty. Suorituskykytestausta varten tarvittaisiin paljon virheellisiä lauseita sekä lause jota on 'yritetty' kirjoittaa. Tällaistä dataa ei kuitenkaan ole avoimesti saatavilla. Esittelen tässä huomioita siitä mitä ohjelma osaa korjata, ja missä puolestaan tulee vihreitä.

### Ohjelma toimii kohtalaisen hyvin
Lauseissa, joissa ei ole montaa kirjoitusvirhettä ja joissa väärinkirjoitetut sanat ovat yleisiä sanoja. Esimerkiksi lause _The weather is nce today_ korjautuu toisessa ehdotuksessa halutuksi _The weather is nice today_.
![weather_is_nice](https://github.com/oheinonen/tiralabra/blob/main/kuvat/weather_is_nice.png)

### Ohjelma ei toimi hyvin
1. Lauseissa, joissa väärinkirjoitetut sanat eivät ole yleisiä sanoja ja kirjoitusasulta samanlaisia sanoja on monta. Näissä ohjelma löytää usein halutun sanan, mutta se ei ole ensimmäisten ehdotusten joukossa. Esim. sanalle _foor_ ehdotetaan lauseessa _take your foor of the table_ vastineeksi _for, food four, door_ ja _floor_, mutta ei _foot_. 

![take_your_foot_of_the_table](https://github.com/oheinonen/tiralabra/blob/main/kuvat/take_your_foor_of_the_table.png)

2. Lauseessa on useita sanoja, joissa on virheitä. Tämä johtuu usein edeltävästä ongelmasta, eli yleisempiä sanoja ehdotetaan ja lause jää kokonaisuudelta sekavaksi.

![i_like_cding_but_haet_tetsing](https://github.com/oheinonen/tiralabra/blob/main/kuvat/i_like_cding_but_haet_tetsing.png)

Tämän lisäksi tarpeeksi pitkällä lauseella ja virheiden määrällä (kun `MAX_TYPOS_IN_SENTENCE` asetettu suureksi) ohjelma hajoaa.

Lisäksi ongelmia ovat esim.
1. Sanaa ei ole sanastossa. Tällöin sitä ei voi löytyä.
2. Väärinkirjoitettu sana on oikea sana. Tällöin ohjelma palauttaa anetun (virheellisen) sanan.
3. Sanassa on monta virhettä. Tämä on ongelma varsinkin lyhyissä sanoissa, sillä niitä paljon, ja hakemiseen kuluu aikaa. Tämän vuoksi jäävät myös ihmiselle helposti tunnistettavat kirjoitusvirheet huomaamatta - esim. _makroekonomics_ -> _macroeconomics_

Ohjelman `SpellCorrector` luokassa on maagiset numerot `MAX_TYPOS_IN_WORD` sekä `MAX_TYPOS_IN_SENTENCE`. Ideaalitilanteessa näitä arvoja ei tarvita, mutta koska ohjelma ei osaa ottaa esimerkiksi kontekstia huomioon, tulee asettaa rajat typojen määrille jotta korjausehdotuksia ei tule liikaa. Mikäli esimerkiksi `MAX_TYPOS_IN_WORD` olisi neljä, tarjoaisi ohjelma nelikirjaimiselle sanalle kaikki nelikirjaimiset sanat niiden yleisyyden mukaan. 
