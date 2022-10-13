## Assignment Prompt
1. Create a new github repo called 'web-scraping' 

2. Using BS4, find at least 2 websites that you want to scrap data from - provide that code within a .py file  

3. In the code, for each website - create at least one dataframe that has structured data 

4. Save each of the dataframes as separate .csv files into a "/data" folder within your repo - be sure to include the .csv files within your repo (make sure they are small, < 25mb) 

4. Include a markdown file in the repo which includes instructions (e.g., what are the required python packages to run this, your approach for scrapping the data - the div/classes/css tags you found to extract the information)

## Approach for webscraping
1. ### Install required packages:
    - import requests
    - from bs4 import BeautifulSoup
    - import pandas as pd

2. ### Look for websites that can be scraped.
    - Websites with simple HTML format
    - Avoid websites that block you from scraping

3. ### Using python loops, gather key information such as article titles, authors, descriptions, and dates.

4. ### Save all the inforamtion gathered to a dataframe, and then into a csv file.

## Tags used for scraping
1. ### gizmodo.py
    - titles = soup.find_all('h2',class_='sc-759qgu-0 cAqwZL cw4lnv-6 hUnBTP')
    - descriptions = soup.find_all('p',class_='sc-77igqf-0 bOfvBY')
    - authors = soup.find_all('div', class_="sc-1jc3ukb-3 kIswQi")
    - dates = soup.find_all('time',class_='uhd9ir-0 eIBTgD')

2. ### everydayhealth.py
    - titles = soup.find_all('h2', class_='category-index-article__title')
    - descriptions = soup.find_all('div',class_='category-index-article__dek')
    - authors = soup.find_all('span', class_='category-index-article__author')
    - dates = soup.find_all('span',class_='category-index-article__date')
    
