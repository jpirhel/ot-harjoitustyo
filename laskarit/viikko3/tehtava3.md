# Tehtävä 3

Ajamiseen liittyvä sekvenssikaavio.

**Huom!** Ei varsinaisesti mallinnettu bensiinin määrän tarkistusta. Tämän voisi kenties tehdä Mermaidin break-toiminnallisuudella. Huomioitu vain loop:issa (While driving).

```mermaid
sequenceDiagram
%%participant Main
%%participant Machine
%%participant FuelTank
%%participant Engine

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

loop While driving (engine is running)
Machine ->> Engine: use_energy()
Engine ->> FuelTank: consume(10)
end

deactivate Engine
deactivate FuelTank
deactivate Machine
deactivate Main
```
