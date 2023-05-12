# Testaus

Sovelluksen luokkia ja niiden toiminnallisuutta testataan **pytest**:illä unit testein.

## Sovelluslogiikka

**harjoitustyo/engine/*.py**

Lähes kaikki toiminnallisuus testataan, toimivalla datalla ja osin virheellisellä datalla. Tämä sisältää sovelluksen toteuttamiseen tarvittavat data classit.

**harjoitustyo/engine/data/*.py**

Dataa käsittelevistä luokista testataan muu toiminnallisuus, paitsi:

- SQLite-tietokannan luontia ei testata
- tietokantaa ei testata synteettisellä (esim. virheellisellä) datalla
- zip_importer:ia ei testata, koska nykyisellä implementaatiolla datan importtaaminen kestää hyvin pitkään (kymmeniä minuutteja)

## Käyttöliittymå

**harjoitustyo/ui/**

tkinter:illä toteutettua käyttöliittymää ei testata.

## Järjestelmätestaus

Järjestelmätestausta varten ei ole erikseen toteutettu ohjelmallisia testejä.

## Asennus ja konfigurointi

Sovelluksen toimivuus on testattu Windows- ja Linux-ympäristössä, varmistan että perustoiminnallisus ei aiheuta virheilmoituksia.

## Sovellukseen jääneet laatuongelmat

Pysäkkiaikataulujen tiedot eivät ole nykyisessä implementaatiossa yhtenevät HSL.fi:ssä olevien pysäkkikohtaisten aikataulujen kanssa. Sovellusta voi pitää siis enemmän esimerkkinä tällaisen sovelluksen toteuttamisesta kuin luotettavana tietolähteenä.
