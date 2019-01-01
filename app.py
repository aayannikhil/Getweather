from selenium import webdriver
from sys import argv
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd


#---------GET INPUT FROM COMMAND LINE ARGV---------#
place = argv[1]
if ',' in place:
    place = place.replace(',', '%20')
date = None
type_forecast = None
if len(argv) == 4:
    date = argv[2]
    type_forecast = argv[3]
elif len(argv) == 3:
    date = argv[2]

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
# driver.get("https://weather.com/search/enhancedlocalsearch?where=" + place + "&loctypes=1/4/5/9/11/13/19/21/1000/1001/1003/&from=hdr")

# BeautifulSoup(driver.page_source, 'lxml')

# myElem = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, 'ul>li>a.styles__itemLink__23h5a')))

# posts = driver.find_elements_by_class_name('styles__itemLink__23h5a')

# d=dict()
# for x, y in enumerate(posts):
#     d[x+1] = y.get_attribute("href")
#     print(str(x+1)+' --> ',y.text)

# desired_place=int(input("\nEnter your desired place number :-> "))
# if desired_place in d.keys():
#     link=d[desired_place]

# getting user choice place link
driver.get('https://weather.com/weather/today/l/INXX0038:1:IN')
place_output = driver.find_element_by_class_name('today_nowcard-location').text
place_time = driver.find_element_by_class_name('today_nowcard-timestamp').text
place_temp = driver.find_element_by_class_name('today_nowcard-temp').text
print(place_output)
print(place_time)
print(place_temp)

driver.close()

