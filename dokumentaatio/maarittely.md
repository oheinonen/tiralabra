# Kirjoitusvirheiden korjaaja
Projektin tarkoituksena on rakentaa algoritmi, joka kykenee korjaamaan kirjoitusvirheet annetusta tekstistä. Ohjelma saa syötteenä lauseen tekstiä. Ohjelma parsii lauseen sanoiksi, ja tarkastaa löytyvätkö kaikki sanat sanastosta. Jos sanaa ei löydy sanastosta, ohjelma korjaa sanan. Lopulta käyttäjälle tulostetaan viisi ehdotusta järjestyksessä eri korjauksilla. 

Ohjelma kirjoitetaan Pythonilla, jota hallitsen kyllin hyvin vertaisarvionteja ajatellen. Opinto-ohjelmani on tietojenkäsittelytieteen kandidaatti ja projektissa käytetty kieli suomi. 

## Käytettävät algoritmit ja tietorakenteet
Kullekin väärinkirjoitetulle sanalle hyödynnetään Damerau–Levenshtein etäisyyttä, jotta löydetään todennäköisin korjattu sana.
Sanaston talletukseen käytetään trie-tietorakennetta, koska siinä Damerau–Levenshtein etäisyttä pystytään tarkastelemaan asteittain sanan etuosan mukaan. Haku voidaan suorittaa ajssa O(L), jossa L on haetun sanan pituus. 

## Tavoitteena olevat aika- ja tilavaativuudet (m.m. O-analyysit)
Tavoitteena ohjelman suoritusajalle on O(N*M), jossa N on lauseen pisimmän sanan pituus ja M solmujen määrä sanastona toimivassa trie-tietorakenteessa.
Ohjelman ajon aikana on tilavaativuus O(1), sillä trie-tietorakenne ei tarvitse hakuun tilaa. 

## Lähteet
- [Damereu-Levenshtein](https://en.wikipedia.org/wiki/Damerau%E2%80%93Levenshtein_distance)
- [Trie-tietorakenne](https://en.wikipedia.org/wiki/Trie)
