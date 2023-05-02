# Käyttöohje

Lataa projektin lähdekoodi githubin releaseista tai kloonaamalla repositorio.

## Ohjelman käynnistäminen

Poetryn riippuvuudet tulee ensin asentaa komennolla `poetry install`.

Ohjelman voi käynnistää komennolla `poetry run invoke start`. Jos tällä ei onnistu, päähakemistosta löytyy myös skripti `run.sh`.

## Toiminnallisuus

Sovelluksen avautuessa avautuu karttanäkymä, jossa näkyy keskellä Kumpulan kampus ja sen ympärillä markereita, jotka 
kuvaavat joukkoliikenteen pysäkkejä. Klikkaamalla pysäkin markeria, vasemmalle avautuu sovelluksen tiedot sekä tiedot 
pysäkille tulevista joukkoliikenteen kulkuvälineistä. 

Sovellus tallentaa sovellusta suljettaessa senhetkisen kartan sijainnin ja zoom-tason sekä aktiivisen pysäkin. 
Seuraavalla käynnistyskerralla nämä tiedot ladataan, joten jos käyttää usein tiettyä pysäkkiä, voi käyttää tätä 
sovellusta tarkastaakseen saapuvat bussit nopeasti.
