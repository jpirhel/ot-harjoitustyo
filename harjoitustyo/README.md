# Harjoitustyö

Tämä on ohjelmistotekniikka-kurssin harjoitustyö. Linkit dokumentaatioon:

[Changelog](dokumentaatio/changelog.md)

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

## Tasks

Nämä ovat ajettavia taskeja, jotka ajetaan seuraavasti:

```
poetry run invoke <task>
```

### start

Käynnistää sovelluksen.

### import-data-from-web

Hakee HSL.zip:in HSL:n web-palvelimelta ja sijoittaa tiedot SQLite-tietokantaan.

### format

Muotoilee lähdekoodia uudelleen autopep8:n avulla.


### quality

Tarkistaa lähdekoodin laadukkuutta pyflakes:in ja pylint:in avulla.


### coverage-report

Generoi HTML-muotoisen raportin lähdekoodin testikattavuudesta käytten coveragea.
