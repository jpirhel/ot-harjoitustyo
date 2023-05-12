## Viikko 1

- idean keksiminen & alustavaa suunnittelua
- alustava implementointi käyttöliittymästä

## Viikko 2

- käyttöliittymän lisäsuunnittelua ja -viilausta
- käytettävien tietojen formaatin tutkimista

## Viikko 3

- implementoitu engine-osuuden data classeja
  - Marker
  - Stop

  Näiden avulla toteutetaan myöhemmin karttaosuuden toiminnallisuutta.

- luotu testejä testaamaan edellämainittujen data classien luomista ja toiminnallisuutta

## Viikko 4

- aloitettu implementoimaan tietojen haku HSL:n web-palvelusta
  - harjoitustyo/engine/data/*
  - harjoitustyo/engine/*
- ei käyttäjälle näkyviä muutoksia
  - testejä ei vielä kirjoitettu testaamaan datan hakua, mutta nämä ovat suunnitelmissa
- tehty pylint- ja autopep8 -korjaukset lähdekoodiin


## Viikko 5

- implementoitu tietojen haku web-palvelusta (poetry run invoke import-data-from-web)
- poetry run invoke start pitäisi nyt toimia
- aloitettu implementoimaan SQLite-tietokannan lukuominaisuutta
  - harjoitustyo/engine/data/reader.py
- implementoitu pysäkkien markerien piirto karttapohjaan
- tehty laaduntarkkailuun liittyviä korjauksia (pylint jne.)
- lisätty testien määrää


## Viikko 6

- parannettu dokumentaatiota
  - lisätty docstringit
- lisätty testejä
- parannettu käyttöliittymää
  - karttaa ohjaavien buttonien tekstit
  - vasemman (control) framen layout
  - callback joka näyttää pysäkin tiedot
  - pysäkin tietoja kontrollinäkymässä

## Viikko 7

- parannettu dokumentaatiota
- lisätty testejä
- parannettu käyttöliittymää
  - toteutettu pysäkkikohtainen aikataulu