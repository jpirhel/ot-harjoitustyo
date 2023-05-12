# Vaatimusmäärittely

## Todo-lista

- **TEHTY** pysäkin aikataulutiedot
- **TEHTY** (reaaliaikainen) minuutteja bussin tuloon -näkymä
- <s>minkä pysäkin kohdalla ko. linjan kulkuneuvo on</s> (ei toteuteta)
- **TEHTY**: kartta
- **TEHTY**: kartan zoom
- <s>suosikit alasvetovalikkoineen</s> (ei toteuteta)
- <s>vapaatekstihaku</s> (ei toteuteta)
- **TEHTY**: testattu sekä Linuxilla että Windowsilla
- **TEHTY** graafinen käyttöliittymä (tkinter)
- **TEHTY**: ei-reaaliaikainen HSL-pysäkkidata tietokantaan
- <s>valitun pysäkin tallennus suljettaessa sovellus</s> (ei toteuteta)
- <s>kartan position ja zoomin tallennus suljettaessa sovellus</s> (ei toteuteta)

## Sovelluksen käyttötarkoitus

Tämän harjoitustyösovelluksen on tarkoitus esittää sovelluksen käyttäjälle aikataulutietoja joukkoliikenteen pysäkeiltä
sekä joukkoliikennelinjoilta.

Sovellukseen kuuluu karttapohja, jonka avulla voi valita Helsingin Seudun Liikenteen alueella
pysäkkejä. Kun pysäkki on valittu, esitetään kyseisen pysäkin aikataulun tiedot. Aikataulutiedoissa näkyy, kuinka monen
minuutin päästä kyseiselle pysäkille on tulossa busseja tai muita joukkoliikennevälineitä.

## Käyttöliittymä

Sovelluksen käyttöliittymässä on kaksi osaa: ikkunan vasemmalla puolella oleva kontrollialue ja oikealla puolella 
oleva kartta-alue. Kontrollialueen avulla valitaan, halutaanko tietoa pysäkeistä vai joukkoliikennelinjoista. Oikealla
puolella nähdään yleiskuva alueesta, joka on käyttäjän kontrolloitavissa. Sovelluksessa voi sekä zoomata että panoroida 
karttaa.

![](kuvat/kayttoliittyma.png?raw=true)

## Toiminnallisuus

Klikkaamalla karttanäkymässä olevaa pysäkin kuvaketta, näytetään kulloinkin valitun pysäkin tiedot vasemmalla olevassa 
näkymässä. Tämä näkymä laskee, kuinka kauan klikkaushetkestä kestää joukkoliikennevälineen saapumiseen. 

Sovellus tarjoilee pysäkkikohtaisen linkin HSL.fi:hin, josta näkyy tarkemmat pysäkkiaikataulut.

## Toteutus

Ohjelma tehdään toimivaksi sekä Linux- että Windows-käyttöjärjestelmillä. Ohjelmassa on graafinen käyttöliittymä.

Koska HSL:n avoimen datan rajapinnat siirtyvät 3.4.2023 käyttäjään kehitysavaimia joita ei haluttu sisällyttää 
sovellukseen, sovellus on toteutettu hyödyntäen HSL:n jakelemaa ei-reaaliaikaista mutta usein päivittyvää pysäkki- ja 
linjatietoa.

## Jatkokehitysideoita

HSL:n tietojen rakenne on melko monimutkainen, ja tähän sovellukseen käytetyn aikataulun puitteissa siihen ei keretty
tutustumaan kunnolla. Sovelluksen näyttämät tiedot eivät vastaa HSL.fi:ssä olevia, joten niitä voi pitää lähinnä 
esimerkkinä siitä, miten sovelluksen voisi toteuttaa.

Tämä on varsin suuri puute, jonka korjaaminen olisi tärkeää sovelluksen oikean toiminnallisuuden kannalta. 
Jatkokehityksen kannalta tosin järjevämpää lienisi HSL:n reaaliaikaisen rajapinnan käyttö. Tätä ei toteutettu, koska
ko. rajapinnan käyttö vaatisi API-avaimen, jota ei halutta sovellukseen sisällyttää.

Reaaliaikaisella rajapinnalla sovellukseen voisi pysäkkikohtaisten aikataulujen lisäksi integroida normaaliaikataulusta
muuttuneet tiedot (joukkoliikennevälineen myöhästyminen, muutokset korjaustöiden tai muiden häiriöiden takia jne.).  
