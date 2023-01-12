<b><p align="center">Raspodijeljeni sustavi</p></b>
<b><p align="center">Projektni zadatak</p></b>
<br>
<br>

Ovaj README.md sadrži osnovne informacije o mikroservisima, kako ih pokrenuti i koristiti.

# Mikroservisi
Ovaj projekt sadrži četiri mikroservisa u Pythonu:

1. app.py - Flask aplikacija koja čita podatke iz JSON datoteke i sprema ih u MySQL bazu podataka. Također, šalje HTTP zahtjeve prema drugim mikroservisima.
2. app2.py - Flask aplikacija koja šalje HTTP zahtjeve prema drugim mikroservisima.
3. app3.py - Flask aplikacija koja filtrira podatke i šalje HTTP zahtjeve prema drugim mikroservisima.
4. app4.py - Flask aplikacija koja prima podatke i stvara datoteke asinkrono.

## Zahtjevi
- Python 3.6 ili noviji
- Flask
- Aiohttp
- mysql-connector-python
- Aiofiles
- requests

## Postavljanje
1. Klonirajte ili preuzmite repozitorij
2. Navigirajte u direktorij projekta
3. Instalirajte potrebne pakete koristeći naredbu "pip": ```pip install -r requirements.txt```
4. Pokrenite svaki mikroservis pokretanjem skripte na svom lokalnom računalu:
```
Windows naredbe:
python app.py
python app2.py
python app3.py
python app4.py

MacOS / Linux naredbe:
python3 app.py
python3 app2.py
python3 app3.py
python3 app4.py
```
5. Pristupite mikroservisima šaljući zahtjeve na odgovarajuće URL-ove u vašem pregledniku ili koristeći alat poput curl-a ili postman-a
Primjeri curl naredbi:

Dohvat prvih 100 redaka iz baze podataka:
```curl http://localhost:5000/get_links```

Poziv e-learning API-ja:
```curl http://localhost:5001/call_elearning_api```

Napomena:

- Morate imati pokrenuti mysql poslužitelj na svom lokalnom računalu ili možete koristiti onaj naveden u kodu, također, osigurajte da se podaci za mysql poslužitelj podudaraju s onima u kodu.
- Prije pokretanja usluge, promijenite IP adrese i portove u kodu kako bi se podudarali s IP-ovima i portovima na kojima će usluge biti pokrenute.

## Upotreba
Prvi mikroservis (app.py) ima dvije rute: '/' i '/get_links'
'/' vraća pozdravnu poruku
'/get_links' vraća prvih 100 redaka baze podataka kao JSON objekt
Drugi mikroservis (app2.py) ima jednu rutu: '/call_elearning_api'
Kada se pozove, šalje zahtjev prvom mikroservisu i prosljeđuje primljene podatke trećem mikroservisu
Treći mikroservis (app3.py) ima dvije rute: '/wt_w' i '/wt_d'
Obje rute primaju JSON objekt koji sadrži listu korisničkih imena, filtriraju korisnička imena prema tome počinju li s 'w' ili 'd' odnosno, te onda prosljeđuju filtrirane podatke četvrtom mikroservisu
Četvrti mikroservis (app4.py) ima jednu rutu: '/gather_data'
Kada se pozove, prima JSON objekt koji sadrži listu podataka i stvara datoteku za svaki element u listi

## Dockerfile
Važno je instalirati Docker prije samog korištenja Dockerfile-ova i kreiranja slika. Upute za instalaciju dostupne su na službenoj stranici Docker-a (https://www.docker.com/).


1. Kopirajte sadržaj svakog Dockerfile.txt datoteke u odgovarajući Dockerfile (npr. sadržaj Dockerfile m0.txt u Dockerfile za mikroservis app.py)

2. Otvorite terminal i navigirajte do direktorija u kojem se nalazi Dockerfile
```
Naredbe za navigaciju između direktorija za sustav windows:
cd - za promjenu trenutnog direktorija
cd.. - za povratak u glavni direktorij
cd naziv_direktorija - za prelazak u direktorij s određenim nazivom
dir - za pregled sadržaja trenutnog direktorija

Naredbe za navigaciju između direktorija za sustav MAC/Linux:
cd - za promjenu trenutnog direktorija
cd.. - za povratak u roditeljski direktorij
cd naziv_direktorija - za prelazak u direktorij s određenim nazivom
ls - za pregled sadržaja trenutnog direktorija
```

3. Izvršite naredbu ```docker build -t ime_slike```. da biste kreirali sliku. Gdje je ime_slike ime koje želite dati slici.

4. Izvršite ```docker run -p port:port ime_slike``` za pokretanje kontenjera s kreiranom slikom. Gdje port predstavlja port koji želite dodijeliti mikroservisu.

5. Ako želite pokrenuti više mikroservisa, kreirajte sliku za svaki mikroservis i pokrenite kontenjer za svaki od njih s različitim portovima.

**Primjer:**
Ako želite pokrenuti mikroservis app.py, prvo kopirajte sadržaj Dockerfile m0.txt u Dockerfile, zatim izvršite docker build -t app . za kreiranje slike, i docker run -p 5000:5000 app za pokretanje kontenjera.
