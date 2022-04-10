# Stuud-cli
### Kirjeldus
Stuud-cli on Pythonis kirjutatud terminali aplikatsioon, mis loob ühenduse Stuudiumiga läbi Chrome webdriveri, kasutades Selenium.
## Kasutamine

1. Esmalt peab laadima chromedriveri ja chromium ühilduva versiooniga
2. Teisalt tuleb installeerida vajalikud andmekogud
´´´sh
pip install -r requirements.txt
´´´
3. Programmi kasutus abi leiab käsuga
´´´sh
python main.py
´´´
VÕI
´´´sh
python main.py --abi
´´´
4. CLI liidese saab käivitada käsuga
´´´sh
python main.py --cli
´´´
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