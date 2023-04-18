# Arkkitehtuuri

Sovellus jakautuu kolmeen pääosioon sekä tietokantaan:

## UI

Tämä osio vastaa sovelluksen graafisesta käyttöliittymästä. Sisältää tkinter:illä toteutetun karttapohjan, sekä toiminnallisuuden pysäkkien ja niiden aikataulujen esittämiseen. Käyttöliittymää ei testata. 

## Engine

Tämä osio on sovelluksen varsinainen sydän. Tässä osiossa on sekä datan importtaamisen liittyvä toiminnallisuus, että UI:n tarvitsema toiminnallisuus erilaisia tietueita varten (Routes, Trips, Stops etc.). Tämän osion laadukkuus varmistetaan testeillä. 

## Tests

Täällä sijaitsevat sovelluksen testit. Sovelluksesta testataan ainoastaan engine-osaa.

## Tietokanta

Tietokanta sijaitsee tiedostossa **database.sqlite**. Tämä on bundlattu sovelluksen mukana. Sovellukseen on rakennettu toiminnallisuus datan importtaamiseen netistä, mutta nopeussyistä tätä toiminnallisuutta ei ole integroitu käyttöliittymään vaan se pitää erikseen käynnistää poetry taskilla (**import-data-from-web**). Datan importtausta ei aikataulusyistä ole optimoitu, joten se kestää huomattavan kauan (tunteja).

# Luokkakaavio

Tähän on merkitty inheritance-, dependency- ja realization-tyypit, saattavat olla hieman epätäsmällisiä.

```mermaid

classDiagram
    class Fetcher {
        fetch()
    }

    class Importer {
        import_data()
    }

    class ZipImporter {
        import_data()
    }

    ZipImporter <|.. Route
    ZipImporter <|.. Stop
    ZipImporter <|.. Trip

    Route <|-- SQLObject
    Stop <|-- SQLObject
    Trip <|-- SQLObject

    class Route {
        str route_id
        str agency_id
        str route_short_name
        str route_long_name
        str route_desc
        str route_type
        str route_url
    }

    class Stop {
        int stop_id
        str stop_code
        str stop_name
        str stop_desc
        float stop_lat
        float stop_lon
        str zone_id
        str stop_url
        int location_type
        int parent_station
        int wheelchair_boarding
        int platform_code
        int vehicle_type
    }

    class Trip {
        str route_id
        str service_id
        str trip_id
        str trip_headsign
        str direction_id
        str shape_id
        str wheelchair_accessible
        str bikes_allowed
        str max_delay
    }

    class Marker {
        str name
        float lat
        float lon
        object obj
    }

    class SQLObject {
        as_list()
        clean_string()
    }

    class Ui

    class Map

    class Control

    class VisibleMarker

    VisibleMarker <|.. Marker

    Marker <|.. Stop

    Stop <.. Trip
    Trip <.. Route

    Ui ..|> Control
    Control ..|> Map

    Map ..|> VisibleMarker
```