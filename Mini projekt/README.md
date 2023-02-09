
<b><p align="center">Raspodijeljeni sustavi</p></b>
<b><p align="center">Projektni zadatak 2</p></b>
<br>
<br>

Ovaj README.md sadrži osnovne informacije o ovom projektnom zadatku, odnosno kako ga pokrenuti i koristiti.

# Master/slave arhitektura
1. Klijent.py (CLIENT): Ovaj kod čita podatke iz datoteke "file-000000000040.json", dijeli kod svakog klijenta na jednake dijelove i šalje zahtjev master servisu za obradu.
2. Master.py (MASTER): Ovaj kod služi kao glavni server za obradu zahtjeva od strane klijenata. Prima zahtjeve od klijenata, dijeli kod na manje dijelove i šalje zahtjeve workerima za obradu.
3. Worker.py (SLAVE): Ovaj kod služi kao worker koji se registrira kod master servisa i prima zahtjeve za obradu od njega. Nakon primitka zahtjeva, worker broji riječi u kodu.

Ukratko, Klijent.py šalje zahtjev master servisu, Master.py obrađuje zahtjeve i šalje ih workerima, a workeri obrađuju podatke i vraćaju rezultate master servisu.

## Zahtjevi
- Python 3.6 ili noviji
- import time
- import random
- from flask import Flask, request
- import requests
- import pandas as pd

## Postavljanje
1. Klonirajte ili preuzmite repozitorij
2. Potrebno je preuzeti i FakeDataset.json datoteku putem poveznice https://www.mediafire.com/file/8iqjc098cdkbrjc/file-000000000040.json/file, te istu postaviti u glavni direktorij
3. Navigirajte u direktorij projekta
5. Pokrenite prvo Master.py, zatim Workere i na kraju pokrenite Klijent.py na svom lokalnom računalu:
```
Windows naredbe:
python Master.py
python Worker.py
python Worker2.py
python Worker3.py
python Worker4.py
python Worker5.py
python Klijent.py

MacOS / Linux naredbe:
python3 Master.py
python3 Worker.py
python3 Worker2.py
python3 Worker3.py
python3 Worker4.py
python3 Worker5.py
python3 Klijent.py
```
5. Provjerite odgovore u konzoli

`

Napomena:
- Prije pokretanja usluge, promijenite IP adrese i portove u kodu kako bi se podudarali s IP-ovima i portovima na kojima će usluge biti pokrenute.

## Upotreba
- Klijent.py je kod koji omogućuje klijentima slanje zahtjeva za brojanje riječi njihovog koda.
- Worker kod (Worker.py, Worker2.py, Worker3.py, Worker4.py i Worker5.py) predstavljaju worker-e i sadrže rutu '/work' koja prima JSON objekt i vraća broj riječi u tome objektu.
- Master.py je glavni servis i on distribuira posao među workerima putem poziva na rutu '/work', a workeri će se registrirati i primati ID putem poziva na rutu '/register' na glavnom mikroservisu.
