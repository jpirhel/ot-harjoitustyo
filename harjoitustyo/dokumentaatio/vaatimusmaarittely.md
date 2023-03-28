# Vaatimusmäärittely

## Sovelluksen käyttötarkoitus

Tämän harjoitustyösovelluksen on tarkoitus esittää sovelluksen käyttäjälle aikataulutietoja joukkoliikenteen pysäkseiltä
sekä joukkoliikennelinjoilta.

Sovellukseen kuuluu karttapohja, jonka avulla voi valita Helsingin Seudun Liikenteen alueella
pysäkkejä. Kun pysäkki on valittu, esitetään kyseisen pysäkin aikataulun tiedot. Aikataulutiedoissa näkyy, kuinka monen
minuutin päästä kyseiselle pysäkille on tulossa busseja.

Pysäkkien lisäksi sovelluksessa on mahdollista valita joukkoliikenteen linjoja, sekä saada näistä aikataulutietoja.
FIXME Sovellus laskee, minkä pysäkin kohdalla ko. linjan kulkuneuvo on. 

## Käyttöliittymä

Sovelluksen käyttöliittymässä on kaksi osaa: ikkunan vasemmalla puolella oleva kontrollialue ja oikealla puolella 
oleva kartta-alue. Kontrollialueen avulla valitaan, halutaanko tietoa pysäkeistä vai joukkoliikennelinjoista. Oikealla
puolella nähdään yleiskuva alueesta, joka on käyttäjän kontrolloitavissa. Sovelluksessa voi sekä zoomata että panoroida 
karttaa.

![](kuvat/kayttoliittyma.png?raw=true)

## Toiminnallisuus

Sovellukseen on mahdollista tallentaa sekä pysäkkejä että bussilinjoja suosikeiksi. Suosikit ovat valittavissa helposti
alasvetovalikosta. Tämän lisäksi sekä pysäkkejä että linjoja on mahdollista hakea vapaatekstihaulla tiedoista.

## Toteutus

Ohjelma tehdään toimivaksi sekä Linux- että Windows-käyttöjärjestelmillä. Ohjelmassa on graafinen käyttöliittymä.

Koska HSL:n avoimen datan rajapinnat siirtyvät 3.4.2023 käyttäjään kehitysavaimia joita ei haluttu sisällyttää 
sovellukseen, sovellus on toteutettu hyödyntäen HSL:n jakelemaa ei-reaaliaikaista mutta usein päivittyvää pysäkki- ja 
linjatietoa.


## Jatkokehitysideoita

Mikäli sovellukseen halutaan sisällyttää HSL:n reaaliaikaisen rajapinnan kutsumahdollisuus avaimineen, on mahdollista 
näyttää pysäkkikohtaiset aikataulut, jotka sisältävät normaaliaikataulusta muuttuneet tiedot (joukkoliikennevälineen 
myöhästyminen, muutokset korjaustöiden tai muiden häiriöiden takia jne.). 
