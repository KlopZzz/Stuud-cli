# Stuud-cli
**Suure tõenäosusega ma lähi tulevikus enam ei panusta sellesse projekti, kuna see täitis mu isikliku ülesande.**
**Edaspidiselt ma commit-in sellesse projekti vähesel määral ning õpieesmärgina. Kui soovid projekti panustada lisa test branch-i pull request ning ma vaatan selle üle, kui antud funktsioon on asjakohane ja töötab, siis ma lisan selle master branch-i.**

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

## Lisa stuud alias bash-i configuration faili

1. Tee kindlaks, et stuud.py on võimalik käivitada
```sh
chmod +x stuud.py
```

2. Lisa alias bashrc faili

```sh
nano ~/.bashrc
```

```sh
alias stuud='/faili/asukoht/stuud.py'
```

3. Värskenda bashrc sätted
```sh
source ~/.bashrc
```

## Lisa stuud alias fish-i shell configuration faili

1. Tee kindlaks, et stuud.py on võimalik käivitada
```sh
chmod +x stuud.py
```

2. Lisa alias fish config faili

```sh
nano ~/.config/fish/config.fish
```

```sh
alias stuud='/faili/asukoht/stuud.py'
```

3. Värskenda fish config sätted
```sh
source ~/.config/fish/config.fish
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
- [x] Stuudium-cli sätted
- [ ] Operatsioon süsteemide toetus
    - [x] Linux
    - [ ] MacOS
    - [x] Windows
- [ ] Automaat seadistused
    - [x] Chromedriver seadistus
    - [ ] Chrome binary seadistus

## Vajalikud repod
* Python3
* Selenium
* Chrome webdriver
* Requests
* lxml

## Disclaimer
NB! Kasutades seda programmi langeb kogu vastutus programmi kasutajale. Programmi looja ei vastuta tekkinud probleemide või kahju eest.
