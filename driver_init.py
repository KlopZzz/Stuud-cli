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
import selenium
import sys
import json
import platform
import logging

global driver

with open('config.json', 'r') as f:
    config = json.load(f)

#edit the data
chromium_set = config['chromium_set']
chromedriver_set = config['chromedriver_set']

#write it back to the file
with open('config.json', 'w') as f:
    json.dump(config, f)

with open('debug.json', 'r') as f:
    config = json.load(f)

debug_i = config['debug_mode']

with open('debug.json', 'w') as f:
    json.dump(config, f)

options = Options()
if debug_i == "False":
    options.add_argument("--headless")
options.add_argument("--no-sandbox")

options.add_argument("window-size=1200,1100")

options.binary_location = chromium_set

driver = webdriver.Chrome(
    chrome_options=options,
    executable_path=chromedriver_set,
)

driver.maximize_window()