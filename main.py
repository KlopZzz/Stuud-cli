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

global ver1
msg_disp = 6
ver1 = 'v1.0.0'

def sisselogimine():

    os.system('clear')
    print('SISSELOGIMINE')
    print(" ")
    usrnme = input('Sisesta Kasutajatunnus: ')
    paswrd = getpass.getpass('Sisesta Parool: ')


    url = 'https://elva.ope.ee/auth/'
    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("window-size=1200,1100")
    options.binary_location = "/usr/bin/chromium"

    global chk1
    chk1 = False
    global driver
    driver = webdriver.Chrome(
        chrome_options=options,
        executable_path='/usr/bin/chromedriver',
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
         valeprl = driver.find_element_by_xpath("//p[@class='status-message error']").text
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
    print('TE OLETE EDUKALT SISSE LOGITUD')
    print(' ')
    print('VALI TEGEVUS')
    print(' ')
    print('[1] Kursuste arv')
    print('[2] Suhtlus')
    print('[3] Kodutöö')
    print(' ')
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

def hmwrk():
    v = '1'
    d = '1'
    os.system('clear')
    z = True
    while z == True:
        try:
            date_hmwrk = driver.find_element_by_xpath('/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/h4['+ v +']').text
            print(' ')
            print(date_hmwrk)
            print(' ')
            v = int(v)
            v = v + 1
            v = str(v)
        except NoSuchElementException:
            try:
                v = int(v)
                v = v + 1
                v = str(v)
                date_hmwrk = driver.find_element_by_xpath('/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/h4['+ v +']').text
                print(' ')
                print(date_hmwrk)
                print(' ')
            except NoSuchElementException:
                z = False


        try:
            content_hmwrk = driver.find_element_by_xpath('/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div['+ d +']/div').text
            print(content_hmwrk)
            d = int(d)
            d = d + 1
            d = str(d)
        except NoSuchElementException:
            try:
                d = int(d)
                d = d + 1
                d = str(d)
                content_hmwrk = driver.find_element_by_xpath('/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div['+ d +']/div').text
                print(content_hmwrk)
            except NoSuchElementException:
                z = False


    print(' ')
    print('PEALEHT >> KODUTÖÖ')
    print(' ')
    print('VALI TEGEVUS')
    print(' ')
    input('VAJUTA ENTER ET TAGSI MINNA...')
    peaaken()

    

def kursus_cnt():
    os.system('clear')
    print('KURSUSTE LOENDUS GÜMNAASIUMILE')
    print(' ')
    driver.get('https://elva.ope.ee/users/summary/'+stdnt_id)
    sleep(1)
    nmbrs = ['1', '2', '3', '4', '5', 'A']
    c = '4'
    global p
    p = '1'
    global b
    b = '1'
    kursus_sum = 0
    g = True
    while g == True:
        if g == False:
            break
        try:
            vrbl = driver.find_element_by_xpath('/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[' + b + ']/td[' + c + ']/span[' + p + ']').text
            if c == '7':
                b = int(b)
                b = b + 1
                b = str(b)
                c = '4'
                p = '1'
            elif vrbl in nmbrs:
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
                    vrbl = driver.find_element_by_xpath('/html/body/div/div[4]/div[1]/div[1]/div[1]/div[2]/div[2]/table/tbody/tr[' + b + ']/td[' + c + ']/span[' + p + ']').text
                except NoSuchElementException:
                    g = False
            else:
                c = int(c)
                c = c + 1
                c = str(c)
                p = '1'
        """
        with open("debug.txt", "a+") as file_object:
            # Move read cursor to the start of file.
            file_object.seek(0)
            # If file is not empty then append '\n'
            data = file_object.read(100)
            if len(data) > 0 :
                file_object.write("\n")
            # Append text at the end of file
            file_object.write('hinne '+vrbl+' || '+'tr '+b+' || '+'td '+c+' || '+'span '+p+' || '+'Kursuse_num '+str(kursus_sum))
        """
        """
        print(vrbl)
        print(' ')
        print('tr ' + b)
        print('td ' + c)
        print('span ' + p)
        print('Kursuste arv ' + str(kursus_sum))
        """
    print ('SUL ON ' + str(kursus_sum) + ' KURSUST')
    print(' ')
    input('VAJUTA ENTER ET MINNA TAGASI...')
    peaaken()




def suhtlus():
    os.system('clear')
    print('PEALEHT >> SUHTLUS')
    print('VALI TEGEVUS')
    print(' ')
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
            sndr = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/h4').text
            date = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/span').text
            title = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/h3').text
            content = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[2]/div[2]').text
            print(' ')
            print('SAATJA: ' + sndr)
            print('KUUPÄEV: ' + date)
            print(' ')
            print('PEALKIRI: ' + title)
            print(' ')
            print(content)
            print(' ')
            print(' ')
            num = int(num)
            num = num + 1
            num = str(num)
        except NoSuchElementException:
            msg_disp = msg_disp + 1
            print('Järjekord')
            print(msg_disp)
            print('Div num')
            print(num)
            try:
                sndr = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/h4').text
                date = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/span').text
                title = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[1]/div[1]/h3').text
                event_date = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[2]/div[2]/span').text
                content = driver.find_element_by_xpath('/html/body/div/div[4]/div[2]/div[3]/div[' + num + ']/div[2]/div[2]/div[3]').text
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
                print('Järjekord')
                print(msg_disp)
                print('Div num')
                print(num)

            

    print(' ')
    input('VAJUTA ENTER, ET TAGASI MINNA TAGASI...')
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
    logout_hover = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/span[2]/img')
    hover = ActionChains(driver).move_to_element(logout_hover)
    hover.perform()
    sleep(1)
    nupp2 = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/span[2]/span/a[3]')
    nupp2.click()
    sleep(1)
    if driver.current_url == 'https://elva.ope.ee/auth/':
        driver.close()
        root.destroy()
        main()
        sleep(1)




def main():
    print('Stuudium-cli ' + ver1)
    print(' ')
    print('Vali tegevus:')
    print(' ')
    print('[1] Logi sisse')
    print('[2] Välju')
    print(' ')
    sel1 = input('Sisesta: ')
    if sel1 == '2':
        exit()
    elif sel1 == '1':
        os.system('clear')
        sisselogimine()
    else:
        os.system('clear')
        input('ANTUD NUMBER POLE VALIKUS....PROOVI UUESTI')
        main()
main()

