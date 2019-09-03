from selenium import webdriver
from sys import argv
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np


#---------GET INPUT FROM COMMAND LINE ARGV---------#
place = argv[1]
if ',' in place:
    place = place.replace(',', '%20')
type_forecast = None
if len(argv) == 3:
    type_forecast = argv[2]

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get("https://weather.com/search/enhancedlocalsearch?where=" +
               place + "&loctypes=1/4/5/9/11/13/19/21/1000/1001/1003/&from=hdr")

    myElem = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'ul>li>a.styles__itemLink__23h5a')))

    posts = driver.find_elements_by_class_name('styles__itemLink__23h5a')

    d = dict()
    for x, y in enumerate(posts):
        d[x+1] = y.get_attribute("href")
        print(str(x+1)+' --> ', y.text)

    desired_place = int(input("\nEnter your desired place number :-> \n"))
    if desired_place in d.keys():
        link = d[desired_place]

    def daily():
        driver.get(link)
        print(driver.find_element_by_class_name('today_nowcard-location').text)
        print(driver.find_element_by_class_name(
            'today_nowcard-timestamp').text)
        print(driver.find_element_by_class_name('today_nowcard-temp').text)
        print(driver.find_element_by_class_name('today_nowcard-phrase').text)
        print(driver.find_element_by_class_name('today_nowcard-feels').text)
        print(driver.find_element_by_class_name('today_nowcard-hilo').text)

    def hourly():
        driver.get("https://weather.com/weather/hourbyhour/l/" + link[36:])
        hourly_place_title = driver.find_element_by_class_name(
            'hourly-page-title').text
        print(hourly_place_title)
        m = []
        p = []
        hourly_info_head = driver.find_elements_by_css_selector(
            '.twc-table>thead>tr>th')
        hourly_info = driver.find_elements_by_css_selector(
            '.twc-table>tbody>tr')
        for x in hourly_info_head:
            p.append(x.text)
        p.insert(1, "DAY")
        s = ','.join(p)
        s = s.replace(',', " ")
        m.append(s)
        for y in hourly_info:
            trim = y.text.replace('\n', ' ')
            m.append(trim)
        for i in m:
            print(i)

    def monthly():
        driver.get("https://weather.com/weather/monthly/l/" + link[36:])
        monthly_place_title = driver.find_element_by_class_name(
            'monthly-page-title').text
        print(monthly_place_title)
        monthly_place_days = driver.find_elements_by_css_selector(
            '.forecast-monthly__days>dt')
        monthly_place_date = driver.find_elements_by_css_selector('.date')
        monthly_place_main = driver.find_elements_by_css_selector('.temps>.hi')
        q, r, s = [], [], []
        for x in monthly_place_days:
            q.append(x.text)
        for y in monthly_place_main:
            r.append(y.text)
        for x in monthly_place_date:
            s.append(x.text)
        for i, j in zip(r, s):
            q.append(j+" -> "+i+"F")
        data = np.array(q)
        data = data.reshape(6, 7)
        df = pd.DataFrame(data)
        print(df.to_string(header=False, index=False))

    if type_forecast == None or type_forecast == "daily":
        daily()
    elif type_forecast == "hourly":
        hourly()
    elif type_forecast == "monthly":
        monthly()

    driver.quit()

except Exception as e:
    print(e)
    driver.quit()
