# Viikkoraportti 3

## Mitä olen tehnyt tällä viikolla?
Lisännyt ohjelmaan oikean sanaston sekä hakemiston, josta selviää sanan yleisyys, sekä laajentanut testejä. Aikaa on viikolla kulunut noin viisi tuntia. 

## Miten ohjelma on edistynyt?
Ohjelma pystyy nyt muodostamaan Levenshteinin etäisyyden avulla hyvän joukon ehdokkaita syötteen korjaamiseksi, sekä järjestämään nämä yleisyyden perusteella.

## Mitä opin tällä viikolla / tänään?
Peter Norvigin [neliosaisen tavan valita sopivin korjaus](http://norvig.com/spell-correct.html). Levenshteinin etäisyys antaa hyvän joukon kandidaatteja, mutta näistä parhaimman valintaan on syytä huomioida sanan yleisyys, sekä millaisia virheitä ihmiset yleensä tekevät.

## Mikä on tuottanut vaikeuksia?
Hyvien datasettien etsiminen.

## Mitä teen seuraavaksi?
- ohjelman pitää ottaa huomioon millaisia virheitä ihminen tekee kirjoittaessaan (tähän tarvitaan jostain dataa) 
- kontekstin huomioiminen ja kokonaisen lauseen korjaaminen (tähänkin pitäisi etsiä sopiva datasetti)
- kahden vierekkäisen kirjaimen vaihtaminen etäisyyttä laskettaessa
