# Viikkoraportti 4

## Mitä olen tehnyt tällä viikolla?
Muokannut Levenshteinin etäisyyden laskemista niin, että se huomioi kahden vierekkäisen kirjaimen vaihdon. Lisäksi syötteenä on nyt lause, ja korjaaja hyödyntää kontekstia ehdottaessaan korjausta. Tämä tapahtuu tarkastelemalla esiintyvien sanaparien yleisyyttä.Aikaa viikolla on kulunut noin 7 tuntia.

Tällä hetkellä ohjelma toimii huonosti, ja sen pitäisi antaa eri typoille eri painoarvot, jotta korjjausehdotukset olisivat hyviä.

## Miten ohjelma on edistynyt?
Ohjelma ottaa sanan sijaan syötteenä lauseen. Pääfunktio on kasvanut, Levenshteinin avulla lasketaan kullekin lauseen sanalle mahdollisia korjauksia, ja näistä muodostetaan ehdokkaita korjatuiksi lauseiksi. Kullekin lauseelle lasketaan todennäköisyys perustuen sanojen ja sanaparien yleisyyteen.

## Mitä opin tällä viikolla / tänään?
Olen lukenut paljon uutta materiaalia miten korjaajaa voisi parantaa, esimerkiksi kontekstin huomioon ottaminen.

## Mikä on tuottanut vaikeuksia?
Päättää mitä priorisoisi kehittäessä ohjelmaa, lisäksi oma prokrastinointi ja työn aloittaminen

## Mitä teen seuraavaksi?
- ohjelman pitää ottaa huomioon millaisia virheitä ihminen tekee kirjoittaessaan (tähän tarvitaan jostain dataa). 
