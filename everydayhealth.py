import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get('https://www.everydayhealth.com/news/')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(soup.prettify())


#Titles
titles = soup.find_all('h2', class_='category-index-article__title')
output_titles = []
for i in titles:
    data = i.text
    output_titles.append(data)
output_titles
len(output_titles)

#Descriptions
descriptions = soup.find_all('div',class_='category-index-article__dek')
output_descriptions = []
for i in descriptions:
    data = i.text
    output_descriptions.append(data)
output_descriptions
len(output_descriptions)

#Authors
authors = soup.find_all('span', class_='category-index-article__author')
output_authors = []
for i in authors:
    data = i.text
    data = data.strip('By') # removes empty space on either side of text
    data = data.replace('\xa0', '')
    data = data.replace('\n', '') # removes empty lines
    output_authors.append(data)
len(output_authors)


#date
dates = soup.find_all('span',class_='category-index-article__date')
output_dates = []
for i in dates:
    data = i.text
    output_dates.append(data)
output_dates
len(output_dates)

# put this together into a dataframe
df = pd.DataFrame({'Titles': output_titles, 'Description': output_descriptions, 'Authors': output_authors, 'Dates': output_dates})
df.to_csv('data/everydayhealth.csv')