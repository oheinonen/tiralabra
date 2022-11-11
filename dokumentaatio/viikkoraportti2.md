# Viikkoraportti 2

## Mitä olen tehnyt tällä viikolla?
Lukenut aiheesta hieman lisää, aloittanut ohjelman tekemisen, ottanut käyttöön pytestin, codecovin sekä pylintin. Aikaa olen käyttänyt noin kuusi tuntia, ensi viikolle allokoitava enemmän jotta ohjelman toteutus pysyy aikataulussa.

## Miten ohjelma on edistynyt?
Tällä hetkellä ohjelma esittää syötetylle sanalle top3 sanaa Levenshtein-etäisyyksineen käytössä olevasta dummy-sanastosta. Toteutus perustuu pitkälti [Steve Hanovin blogipostaukseen](http://stevehanov.ca/blog/?id=114). 

## Mitä opin tällä viikolla / tänään?
Hyvää kertausta poetry projektin alustamisesta (testaus, checkstyle jne.) sekä Hanovin esittämän simppelin rekursiivisen ratkaisun Levenshteinin etäisyyden laskemiseen.

## Mikä jäi epäselväksi tai tuottanut vaikeuksia?
Alku on ollut hieman tahmeaa, mutta yksittäisiä isompia vaikeuksia ja/tai epäselvyyksiä ei ole ollut. 

## Mitä teen seuraavaksi?
Seuraavaksi ohjelman on tarkoitus käyttää oikeaa sanastoa.
Sen jälkeen seuraavia askelia ovat:
- todennäköisimmän sanan valinta useiden joukosta
- kahden vierekkäisen kirjaimen vaihtaminen etäisyyttä laskettaessa (poiston, lisäämisen tai yksittäisen vaihtamisen lisäksi)
- kokonaisen lauseen korjaaminen
