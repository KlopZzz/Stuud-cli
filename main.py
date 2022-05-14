from selenium import webdriver
from lxml import html
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import requests
import getpass
import selenium
import sys
import json
import statistics
import graphs as gr

global ver1
global avrg

msg_disp = 6
ver1 = 'v0.1.1'

with open('config.json', 'r') as f:
    config = json.load(f)
global chromium_set
global chromedriver_set
global school_var
global os_sel
global os_clear

#edit the data
chromium_set = config['chromium_set']
chromedriver_set = config['chromedriver_set']
school_var = config['school_var']
os_sel = config['os_sel']

#write it back to the file
with open('config.json', 'w') as f:
    json.dump(config, f)

if os_sel = "Linux":
    os_clear = "clear"
elif os_sel = "Windows":
    os_clear = "cls"

def sisselogimine():

    os.system(os_clear)
    print('SISSELOGIMINE\n')
    usrnme = input('Sisesta Kasutajatunnus: ')
    paswrd = getpass.getpass('Sisesta Parool: ')


    url = school_var
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("window-size=1200,1100")
    options.binary_location = chromium_set

    global chk1
    chk1 = False
    global driver
    driver = webdriver.Chrome(
        chrome_options=options,
        executable_path=chromedriver_set,
    )
    driver.maximize_window()
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#username"))).send_keys(usrnme)
    driver.find_element_by_css_selector("input#password").send_keys(paswrd)
    driver.find_element_by_css_selector("input.button").click()

    os.system('clear')
    print('SISSELOGIMINE PALUN OODAKE')
    sleep(2)
    
    try:
         valeprl = driver.find_element(By.XPATH, "//p[@class='status-message error']").text
    except NoSuchElementException:
        chk1 = True

    if chk1 == True:
        peaaken()
    else:
        driver.close()
        os.system('clear')
        print('Sisestatud kasutajatunnus või parool on vale')
        input("Vajuta enter et proovida uuesti...")
        sisselogimine()



def peaaken():

    driver.get('https://elva.ope.ee/auth/')
    os.system('clear')
    print('TE OLETE EDUKALT SISSE LOGITUD\n')
    print('VALI TEGEVUS\n')
    print('[1] Kursuste arv')
    print('[2] Suhtlus')
    print('[3] Kodutöö')
    #print('[4] Õpilase tulemuste graafikud')
    print('[5] Välju\n')
    crnt_url = driver.current_url
    j = 22
    global stdnt_id
    stdnt_id = ''
    s = False
    while s == False:
        try:
            stdnt_id = stdnt_id + crnt_url[j]
            j = j + 1
        except IndexError:
            s = True


    print('ÕPILASE ID STUUDIUMIS: ' + stdnt_id)
    sel2 = input('Sisesta: ')


    if sel2 == '1':
        kursus_cnt()
    elif sel2 == '2':
        suhtlus()
    elif sel2 == '3':
        hmwrk()
    elif sel2 == '5':
        exit()
"""
def graphs_i():

    os.system('clear')
    print('GRAAFIKUD\n')
    print('VALI TEGEVUS\n')
    print('[1] Kursuste arv')

    exit()
"""

def hmwrk():
    v = '1'
    d = '1'
    os.system('clear')
    tst = d

    while True:
        try:
            date_hmwrk = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/h4['+ v +']').text
            print(' ')
            print(date_hmwrk)
            print(' ')
            v = int(v)
            v = v + 1
            v = str(v)
        except NoSuchElementException:
            break
        
        try:
            content_test = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div['+ tst +']')
            val = content_test.get_attribute("data-date")
            content_test1 = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div['+ str(int(tst)+1) +']')
            val2 = content_test1.get_attribute("data-date")
            tst = int(tst)
            tst = tst + 1
            tst = str(tst)
            ac = 1
            while val == val2:
                try:
                    ac = ac + 1
                    content_test = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div['+ tst +']')
                    val = content_test.get_attribute("data-date")
                    content_test1 = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div['+ str(int(tst)+1) +']')
                    val2 = content_test1.get_attribute("data-date")
                    tst = int(tst)
                    tst = tst + 1
                    tst = str(tst)
                except NoSuchElementException:
                    break
            
            for i in range(ac):
                try:
                    content_hmwrk = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div['+ d +']/div').text
                    print(' ')
                    print(content_hmwrk)
                    print(' ')
                    d = int(d)
                    d = d + 1
                    d = str(d)
                except NoSuchElementException:
                    break
        except NoSuchElementException:
            break
    
    print()
    print('PEALEHT >> KODUTÖÖ\n')
    print('VALI TEGEVUS\n')
    input('VAJUTA ENTER ET TAGASI MINNA...')
    peaaken()

    

def kursus_cnt():
    os.system('clear')
    print('KURSUSTE LOENDUS GÜMNAASIUMILE\n')

    with open('grading.json', 'r') as f:
        config = json.load(f)

    #edit the data
    cours_sum = config['course_sum']
    average_grade = config['average_grade']

    #write it back to the file
    with open('grading.json', 'w') as f:
        json.dump(config, f)

    if cours_sum != 0 and average_grade != 0:
        print("Sul on " + str(cours_sum) + " kursust!")
        print("Su üldine keskmine hinne on " + str(average_grade))
        print()
        val = input("Kas sa soovid alustada kursuse loendust uuesti? [y/n]: ")
        if val == 'y':

            driver.get('https://elva.ope.ee/users/summary/'+stdnt_id)
            sleep(1)

            avrg = []
            nmbrs = ['1', '2', '3', '4', '5', 'A']
            c = '4'
            p = '1'
            b = '1'
            kursus_sum = 0
            z = 0
            g = True

            while g == True:
                if g == False:
                    break
                try:
                    vrbl = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[' + b + ']/td[' + c + ']/span[' + p + ']').text
                    if c == '7':
                        b = int(b)
                        b = b + 1
                        b = str(b)
                        c = '4'
                        p = '1'
                    elif vrbl in nmbrs:
                        try:
                            z = int(vrbl)
                            avrg.append(z)
                        except ValueError:
                            pass
                        kursus_sum = kursus_sum + 1
                        p = int(p)
                        p = p + 1
                        p = str(p)
                    elif len(vrbl) == 2:
                        kursus_sum = kursus_sum + 2
                        p = int(p)
                        p = p + 1
                        p = str(p)
                    else:
                        p = int(p)
                        p = p + 1
                        p = str(p)
                except NoSuchElementException:
                    if c == '7':
                        b = int(b)
                        b = b + 1
                        b = str(b)
                        c = '4'
                        p = '1'
                        try:
                            vrbl = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[' + b + ']/td[' + c + ']/span[' + p + ']').text
                        except NoSuchElementException:
                            g = False
                    else:
                        c = int(c)
                        c = c + 1
                        c = str(c)
                        p = '1'
            
            config = {"average_grade": statistics.mean(avrg), "course_sum": kursus_sum}
            with open('grading.json', 'w') as f:
                json.dump(config, f)
            kursus_cnt()

        elif val == 'n':
            peaaken()
    if cours_sum == 0 and average_grade == 0:
        driver.get('https://elva.ope.ee/users/summary/'+stdnt_id)
        sleep(1)

        avrg = []
        nmbrs = ['1', '2', '3', '4', '5', 'A']
        c = '4'
        p = '1'
        b = '1'
        kursus_sum = 0
        z = 0
        g = True

        while g == True:
            if g == False:
                break
            try:
                vrbl = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[' + b + ']/td[' + c + ']/span[' + p + ']').text
                if c == '7':
                    b = int(b)
                    b = b + 1
                    b = str(b)
                    c = '4'
                    p = '1'
                elif vrbl in nmbrs:
                    try:
                        z = int(vrbl)
                        avrg.append(z)
                    except ValueError:
                        pass
                    kursus_sum = kursus_sum + 1
                    p = int(p)
                    p = p + 1
                    p = str(p)
                elif len(vrbl) == 2:
                    kursus_sum = kursus_sum + 2
                    p = int(p)
                    p = p + 1
                    p = str(p)
                else:
                    p = int(p)
                    p = p + 1
                    p = str(p)
            except NoSuchElementException:
                if c == '7':
                    b = int(b)
                    b = b + 1
                    b = str(b)
                    c = '4'
                    p = '1'
                    try:
                        vrbl = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[' + b + ']/td[' + c + ']/span[' + p + ']').text
                    except NoSuchElementException:
                        g = False
                else:
                    c = int(c)
                    c = c + 1
                    c = str(c)
                    p = '1'

        config = {"average_grade": statistics.mean(avrg), "course_sum": kursus_sum}
        with open('grading.json', 'w') as f:
                json.dump(config, f)
        
        print ('SUL ON ' + str(kursus_sum) + ' KURSUST')
        print ('Su üldine keskmine hinne on ' + str(statistics.mean(avrg)))
        print(' ')
        input('VAJUTA ENTER ET MINNA TAGASI...')
        peaaken()




def suhtlus():
    os.system('clear')
    print('PEALEHT >> SUHTLUS')
    print('VALI TEGEVUS\n')
    print('[1] Otsi sõnumit')
    print('[2] Saada sõnum')
    print('[3] Muuda sätteid')
    print('[4] Kuva sõnumid')
    print('[5] Tagasi')
    print(' ')

    sel3 = input('Sisesta: ')

    if sel3 == '1':
        print()
    elif sel3 == '2':
        print()
    elif sel3 == '3':
        suhtlus_settings()
    elif sel3 == '4':
        disp_msg()
    elif sel3 == '5':
        peaaken()

def disp_msg():
    global msg_disp
    i = 0
    num = '2'
    driver.get('https://elva.ope.ee/suhtlus/')
    sleep(2)
    for i in range(msg_disp):
        try:
            sndr = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/h4').text
            date = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/span').text
            title = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/h3').text
            content = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[2]/div[2]').text
            print(' ')
            print('SAATJA: ' + sndr + "\n")
            print('KUUPÄEV: ' + date + "\n")
            print('PEALKIRI: ' + title + "\n")
            print(content)
            print('\n')
            num = int(num)
            num = num + 1
            num = str(num)
        except NoSuchElementException:
            msg_disp = msg_disp + 1

            try:
                sndr = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/h4').text
                date = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/span').text
                title = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/h3').text
                event_date = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[2]/div[2]/span').text
                content = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[2]/div[3]').text
                print(' ')
                print('SAATJA: ' + sndr)
                print('KUUPÄEV: ' + date)
                print(' ')
                print('PEALKIRI: ' + title)
                print(' ')
                print('TOIMUMIS KUUPÄEV: ' + event_date)
                print(content)
                print(' ')
                print(' ')
            except NoSuchElementException:
                num = int(num)
                num = num + 1
                num = str(num)
            

    print(' ')
    input('VAJUTA ENTER, ET MINNA TAGASI...')
    suhtlus()

def suhtlus_settings():
    
    os.system('clear')
    print('PEALEHT >> SUHTLUS >> SÄTTED')
    print('VALI TEGEVUS')
    print(' ')
    print('[1] Muuda näidatavate sõnumite kogust')
    print('[2] Tagasi')
    print('[3] Tagasi pealehele')
    print(' ')

    sel4 = input('Sisesta: ')
    if sel4 == '1':
        while True:
            os.system('clear')
            print('VALI KUVATAVATE SÕNUMITE ARV  1 - 25')
            print('VAIKESÄTE ON 5')
            print(' ')
            print('[0] Tagasi')
            msg_disp = int(input('Sisesta: '))
            if msg_disp == 0:
                break
            elif msg_disp > 25 or msg_disp < 1:
                print('Sisestatud number peab olema 1 - 25 vahel!')
            else:
                print('Kuvatavate sõnumite arv edukalt muudetud!')
                sleep(2)
                break

        suhtlus_settings()
    if sel4 == '2':
        suhtlus()
    elif sel4 == '3':
        peaaken()



def v2ljalogi():
    logout_hover = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/span[2]/img')
    hover = ActionChains(driver).move_to_element(logout_hover)
    hover.perform()
    sleep(1)
    nupp2 = driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/span[2]/span/a[3]')
    nupp2.click()
    sleep(1)
    if driver.current_url == 'https://elva.ope.ee/auth/':
        driver.close()
        root.destroy()
        main()
        sleep(1)

def helpcli():
    print("""

    Stuudium-CLI käsurea argumendid

    python main.py arg1 arg2


    --abi --help / python main.py --abi / Toob esile praeguse akna

    --cli / python main.py --cli / Käivitab Stuudiumi-CLI liidese
    
    """)

def glob_settings():
    

    print("Globaalsed sätted\n")
    print("[1] Chromedriver asukoht - Hetke seadistus: " + chromedriver_set)
    print("[2] Chromium asukoht - Hetke seadistus: " + chromium_set)
    print("[3] Kooli Stuudiumi veebilehe aadress - Hetke seadistus: " + school_var)
    print("[4] Operatsiooni süsteemi valimine - Hetke seadistus: " + os_sel)
    print('[5] Tagasi\n')

    opt1 = input('Sisesta: ')
    print()
    if opt1 == '1':

        opt2 = input('Sisesta sobiv Chromedriver asukoht: ')
        if opt2 == "0":
            glob_settings()

        config = {"school_var": school_var, "chromium_set": chromium_set, "chromedriver_set": opt2, "os_sel": os_sel}

        with open('config.json', 'w') as f:
            json.dump(config, f)
        glob_settings()

    elif opt1 == '2':
        opt2 = input('Sisesta sobiv Chromium asukoht: ')
        if opt2 == "0":
            glob_settings()

        config = {"school_var": school_var, "chromium_set": opt2, "chromedriver_set": chromedriver_set, "os_sel": os_sel}

        with open('config.json', 'w') as f:
            json.dump(config, f)
        
        glob_settings()
    elif opt1 == '3':
        opt2 = input('Sisesta sobiv kooli Stuudiumi veebilehe aadress: ')
        if opt2 == "0":
            glob_settings()

        config = {"school_var": opt2, "chromium_set": chromium_set, "chromedriver_set": chromedriver_set, "os_sel": os_sel}

        with open('config.json', 'w') as f:
            json.dump(config, f)
        glob_settings()

    elif opt1 == '4':
        os.system("clear")
        print("[1] Linux")
        print("[2] Windows")
        print("[3] Tagasi")
        opt2 = input('Vali operatsioonisüsteem: ')
        if opt2 == "1":
            sel_os = "Linux"
        elif opt2 == "2":
            sel_os = "Windows"
        elif opt2 == "3":
            glob_settings()

        config = {"school_var": school_var, "chromium_set": chromium_set, "chromedriver_set": chromedriver_set, "os_sel": sel_os}

        with open('config.json', 'w') as f:
            json.dump(config, f)
        glob_settings()

    elif opt1 == '5':
        main()

def main():
    os.system('clear')
    print('Stuudium-cli ' + ver1 + "\n")
    print('Vali tegevus:\n')
    print('[1] Logi sisse')
    print('[2] CLI abi')
    print('[3] Seadistus\n')
    print('[4] Välju\n')

    sel1 = input('Sisesta: ')

    if sel1 == '4':
        exit()
    elif sel1 == '1':
        os.system('clear')
        sisselogimine()
    elif sel1 == '2':
        helpcli()
    elif sel1 == '3':
        glob_settings()
    else:
        os.system('clear')
        input('ANTUD NUMBER POLE VALIKUS....PROOVI UUESTI')
        main()

try:
    if str(sys.argv[1]) == '--help' or str(sys.argv[1]) == '--abi':
        helpcli()
    elif str(sys.argv[1]) == '--cli':
        main()
    elif len(sys.argv) == 1:
        helpcli()
    else:
        print("Antud argumendid ei kehti!")
    exit()
except IndexError:
    helpcli()
    exit()

