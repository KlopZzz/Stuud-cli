from time import sleep
import os
import sys
import json
import statistics
import logging

def count():

    input("ENTER")

    global kursus_sum
    global avrg_g
    with open('grading.json', 'r') as f:
        config = json.load(f)

    #edit the data
    cours_sum = config['course_sum']
    average_grade = config['average_grade']

    #write it back to the file
    with open('grading.json', 'w') as f:
        json.dump(config, f)

    from stuud import driver
    from stuud import school_var
    from stuud import stdnt_id

    driver.get(school_var+'users/summary/'+ stdnt_id)
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

    avrg_g = statistics.mean(avrg)

    config = {"average_grade": statistics.mean(avrg), "course_sum": kursus_sum}
    with open('grading.json', 'w') as f:
        json.dump(config, f)

    input("ENTER")

    return[kursus_sum, avrg_g]

run_once = 0
while 1:
    if run_once == 0:
        count()
        run_once = 1
    break
