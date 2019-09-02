from sys import argv
import requests
from datetime import datetime
from bs4 import BeautifulSoup


#---------GET INPUT FROM COMMAND LINE ARGV---------#
place=argv[1]
if ',' in place:
    place = place.replace(',', '%')
date=None
type_forecast=None
if len(argv)==4:
    date=argv[2]
    type_forecast=argv[3]
elif len(argv)==3:
    date=argv[2]

#---------FUNCTION TO GET HTML FROM URL---------#
def getHTML(url):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'lxml')




# imdb_home_page = getHTML("https://weather.com/search/enhancedlocalsearch?where="+ inp + "& loctypes=1/4/5/9/11/13/19/21/1000/1001/1003/&from=hdr")
# find_show_id = imdb_home_page.findAll('li', class_='styles__itemLink__23h5a')


# print(find_show_id)
