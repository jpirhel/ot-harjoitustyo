# Tehtävä 3

Ajamiseen liittyvä sekvenssikaavio.

**Huom!** Ei varsinaisesti mallinnettu bensiinin määrän tarkistusta. Tämän voisi kenties tehdä Mermaidin break-toiminnallisuudella. Huomioitu vain loop:issa (While driving).

Tehtävän koodissa ei myöskään ollut loop:ia, vaan enginen use_energy():ä kutsutaan vain kerran. Tuntui kuitenkin luontevalta laittaa mukaan tuo loop, koska ajaminen lienee toimintaa, joka jatkuu kunnes bensa loppuu tai ajaminen keskeytetään.

```mermaid
sequenceDiagram

activate Main

Main ->> +Machine: __init__()

activate Machine

Machine ->> +FuelTank: __init__()

Machine ->> FuelTank: fill(40)

Machine ->> +Engine: __init__(self._tank)

Main ->> Machine: drive()

Machine ->> Engine: start()

Engine ->> FuelTank: consume(5)

Machine ->> Engine: is_running()

Engine ->> FuelTank: fuel_contents
FuelTank -->> Engine: 35

Engine -->> Machine: True

loop While driving (engine is running)
    Machine ->> Engine: use_energy()
    Engine ->> FuelTank: consume(10)
end

deactivate Engine
deactivate FuelTank
deactivate Machine
deactivate Main
```
