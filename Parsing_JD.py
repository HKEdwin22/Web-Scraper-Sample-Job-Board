'''
This script aims at parsing the info of jobs of the sample page: https://news.ycombinator.com/jobs

- Background -
In the first trial, we parsed only 30 items from the webpage. We noticed that each page displays 30 items only, with a button "More" in the bottom.
When the button is clicked, the next 30 items will be displayed. 
When the last item is displayed and the button is clicked again, an error page appears with a button "Reload".

- Method -
1. Parse the page with Beautifulsoup
2. Click the button "More" with Selenium Webdriver
3. Repeat step 1 and 2 until reaching the error page
4. Save the results into a csv file
'''

# Import libraries
import pandas as pd

import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

HEADERS ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

cont = True
nb_items = 0

while cont:
    if nb_items == 0: # for 1st loop
        # Open the webpage
        url = 'https://news.ycombinator.com/jobs'
        driver = webdriver.Chrome()
        driver.get(url)
    else:
        try:
            More = driver.find_element(By.LINK_TEXT, 'More')
        except:
            cont = False
            break
        else:
            # Click the link "More"
            More.click()
            
            # Update the webpage link
            driver.find_element(By.LINK_TEXT, 'More')
            url = driver.current_url

    # Give time for reading the webpage (Optional)
    # time.sleep(3)

    # Parse the page
    response = requests.get(url, headers=HEADERS)
    content = BeautifulSoup(response.content, 'lxml')

    titleline = content.find_all(class_='titleline')
    if nb_items == 0: # for 1st loop
        JD = [x.text for x in titleline] 
        nb_items += 30
    else:
        for x in titleline:
            nb_items += 1
            JD.append(x.text)
    
    # Obtain the link of "More"
    More = content.find(class_ = 'morelink')
    More_link = More.get('href')

print(f'{len(JD)} out of {nb_items} items are extracted in total.')
if len(JD) == nb_items:
    dict = {'Job Descriptions': JD}
    df = pd.DataFrame(dict)
    df.to_csv('JD.csv')
    
pass
