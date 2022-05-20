# Stuud-cli
### Kirjeldus
Stuud-cli on Pythonis kirjutatud terminali aplikatsioon, mis loob ühenduse Stuudiumiga läbi Chrome webdriveri, kasutades Selenium.
## Kasutamine

1. Esmalt peab laadima chromedriveri ja chromium binary, ühilduva versiooniga
2. Teisalt tuleb config.json sisestada vajalikud andmed
    * school_var - Kooli Stuudiumi veebiaadress (Vaikesätteks on Elva Gümnaasiumi aadress)(Kõik stuudiumi aadressid ei pruugi õigesti töötada)
    * (chromium_var - Chromium aplikatsiooni asukoht) - aegunud seadistus, saab teostada ka programmis
    * (chromedriver_var - Chromedriver asukoht) - aegunud seadistus, saab teostada ka programmis
    * os_sel - operatsioonisüsteemi säte.

Error käsitluse ja logimise saab seadistada debug.json failis
* debug_mode - vaikesäte "False" - vastandsäte "True"
* logging_mode - vaikesäte "False" - vastandsäte "True"


Chromedriver ja Chromium vaikesätteks on Linuxis olevad käivituskohad.

Kõiki mainitud seadistusi on võimalik muuta ka läbi CLI liidese
```sh
python stuud.py --cli
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
4. Programmi kasutusabi leiab käsuga
```sh
python stuud.py
```
VÕI
```sh
python stuud.py --abi
```
5. CLI liidese saab käivitada käsuga
```sh
python stuud.py --cli
```
## Töötavad funktsioonid
- [x] Sisselogimis liides
- [ ] Kursuste loendus
    - [x] Kursuste loendamine (gümnaasium)
    - [x] Keskmise hinde arvutamine (gümnaasium)
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
    - [x] Windows

## Vajalikud repod
* Python3
* Selenium
* Chrome webdriver
* Requests
* lxml

## Disclaimer
NB! Kasutades seda programmi langeb kogu vastutus programmi kasutajale. Programmi looja ei vastuta tekkinud probleemide või kahju eest.
