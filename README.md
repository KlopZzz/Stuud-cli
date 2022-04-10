# Stuud-cli
### Kirjeldus
Stuud-cli on Pythonis kirjutatud terminali aplikatsioon, mis loob ühenduse Stuudiumiga läbi Chrome webdriveri, kasutades Selenium.
## Kasutamine

1. Esmalt peab laadima chromedriveri ja chromium ühilduva versiooniga
2. Teisalt tuleb config.json sisestada vajalikud andmed
    * school_var - Kooli Stuudiumi veebiaadress (Vaikesätteks on Elva Gümnaasiumi aadress)
    * chromium_var - Chromium aplikatsiooni asukoht
    * chromedriver_var - Chromedriver asukoht

Chromedriver ja Chromium vaikesäteks on Linuxis olevad käivituskohad.

Kõike mainitud seadistusi on võimalik muuta ka läbi CLI liidese
```sh
python main.py --cli
```
Vali tegevuseks Seadistus (nr. 3)
```sh
Vali tegevus:

[1] Logi sisse
[2] CLI abi
[3] Seadistus

[4] Välju

Sisesta: 3
```
Vali sobiv seadistus nr. ning järgi juhiseid
```sh
Globaalsed sätted

[1] Chromedriver asukoht - Hetke seadistus: /usr/bin/chromedriver
[2] Chromium asukoht - Hetke seadistus: /usr/bin/chromium
[3] Kooli Stuudiumi veebilehe aadress - Hetke seadistus: https://elva.ope.ee
[4] Tagasi

Sisesta:
```

3. Järgnevalt tuleb installeerida vajalikud andmekogud
```sh
pip install -r requirements.txt
```
4. Programmi kasutus abi leiab käsuga
```sh
python main.py
```
VÕI
```sh
python main.py --abi
```
5. CLI liidese saab käivitada käsuga
```sh
python main.py --cli
```
## Töötavad funktsioonid
- [x] Sisselogimis liides
- [ ] Kursuste loendus
    - [x] Kursuste loendamine (gümnaasium)
    - [ ] Keskmise hinde arvutamine
- [ ] Kodutööde funktsioonid
- [ ] 'Suhtlus' funktsioonid
    - [x] Hiljutiste sõnumite kuvamine
    - [ ] Sõnumite saatmine
    - [ ] Automaat seadistused
- [ ] Andmebaasi funktsioonid
- [x] Stuudium-cli sätted
- [ ] Operatsioon süsteemide toetus
    - [x] Linux
    - [ ] MacOS
    - [ ] Windows

## Vajalikud repod
* Python3
* Selenium
* Chrome webdriver
* Requests
* lxml