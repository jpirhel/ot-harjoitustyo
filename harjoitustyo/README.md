# Harjoitustyö

Tämä on ohjelmistotekniikka-kurssin harjoitustyö. Linkit dokumentaatioon:

[Changelog](dokumentaatio/changelog.md)

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

## Sovelluksen käynnistäminen

Sovelluksen käynnistys on testattu Cubbli Linuxilla komennolla

```
poetry run invoke start
```

Mikäli tämä ei syystä tai toisesta toimi, lähdekoodissa on myös käynnistysskripti 

```
./run.sh
```
jolla sovellus käynnistyy.

## Tasks

Nämä ovat ajettavia taskeja, jotka ajetaan seuraavasti:

```
poetry run invoke <task>
```

### start

Käynnistää sovelluksen.

### import-data-from-web

**HUOM!** Datan importtaus kestää todella pitkään, joten tätä ei kannattane ajaa. Sovelluksen mukana jaellaan valmis tietokanta.

Hakee HSL.zip:in HSL:n web-palvelimelta ja sijoittaa tiedot SQLite-tietokantaan.

### format

Muotoilee lähdekoodia uudelleen autopep8:n avulla.


### quality

Tarkistaa lähdekoodin laadukkuutta pyflakes:in ja pylint:in avulla.


### coverage-report

Generoi HTML-muotoisen raportin lähdekoodin testikattavuudesta käytten coveragea.
