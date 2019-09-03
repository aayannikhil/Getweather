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

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome

    driver.get("https://weather.com/search/enhancedlocalsearch?where=" + place + "&loctypes=1/4/5/9/11/13/19/21/1000/1001/1003/&from=hdr")

    myElem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'ul>li>a.styles__itemLink__23h5a')))

    posts = driver.find_elements_by_class_name('styles__itemLink__23h5a')

    d=dict()
    for x, y in enumerate(posts):
        d[x+1] = y.get_attribute("href")
        print(str(x+1)+' --> ',y.text)

    desired_place=int(input("\nEnter your desired place number :-> \n"))
    if desired_place in d.keys():
        link=d[desired_place]

    # getting user choice place link
    def daily():
        driver.get(link)
        place_output = driver.find_element_by_class_name('today_nowcard-location').text
        place_time = driver.find_element_by_class_name('today_nowcard-timestamp').text
        place_temp = driver.find_element_by_class_name('today_nowcard-temp').text
        place_phrase = driver.find_element_by_class_name('today_nowcard-phrase').text
        place_feels = driver.find_element_by_class_name('today_nowcard-feels').text
        place_hilo = driver.find_element_by_class_name('today_nowcard-hilo').text

        # daily forecast
        print(place_output)
        print(place_time)
        print(place_temp)
        print(place_phrase)
        print(place_feels)
        print(place_hilo)

    # hourly
    # driver.get("https://weather.com/weather/hourbyhour/l/" + link[36:])
    driver.get("https://weather.com/weather/hourbyhour/l/" + "INXX0038:1:IN")

    hourly_place_title = driver.find_element_by_class_name('hourly-page-title').text
    main_info = driver.find_element_by_class_name('styles__wwirData__qsqOf').text
    m=[]
    p=[]
    hourly_info = driver.find_elements_by_css_selector('.twc-table>thead>tr>th')
    hourly_info1 = driver.find_elements_by_css_selector('.twc-table>tbody>tr')
    for x in hourly_info:
        p.append(x.text)
    p.insert(1, "DAY")
    s = ','.join(p)
    s = s.replace(',', " ")
    m.append(s)

    for y in hourly_info1:
        trim=y.text.replace('\n',' ')
        m.append(trim)

    print(hourly_place_title)
    print(main_info)
    # print(hourly_info)
    # print(hourly_info1)
    
    for i in m:
        print(i)

    driver.quit()

except Exception as e:
    print(e)
    driver.quit()


