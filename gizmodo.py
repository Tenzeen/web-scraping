from matplotlib.pyplot import title
import requests
from bs4 import BeautifulSoup
import pandas as pd


page = requests.get('https://gizmodo.com/tech/news')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

# print pretty
print(soup.prettify())


#Titles
titles = soup.find_all('h2',class_='sc-759qgu-0 cAqwZL cw4lnv-6 hUnBTP')
output_titles = []
for i in titles:
    data = i.text
    output_titles.append(data)
output_titles
len(output_titles)

#Descriptions
descriptions = soup.find_all('p',class_='sc-77igqf-0 bOfvBY')
output_descriptions = []
for i in descriptions:
    data = i.text
    output_descriptions.append(data)
output_descriptions
len(output_descriptions)

#Authors
authors = soup.find_all('div', class_="sc-1jc3ukb-3 kIswQi")
output_authors = []
for i in authors:
    data = i.text
    data = data.strip('By') # removes empty space on either side of text
    data = data.replace('\xa0', ' ') #first article had two authors which made parts of it not readable. Used replace to remove the unreadable portion.
    data = data.replace('\n', '') # removes empty lines
    output_authors.append(data)
len(output_authors)


#date
dates = soup.find_all('time',class_='uhd9ir-0 eIBTgD')
output_dates = []
for i in dates:
    data = i.text
    output_dates.append(data)
output_dates
len(output_dates)

## put this together into a dataframe
df = pd.DataFrame({'Titles': output_titles, 'Description': output_descriptions, 'Authors': output_authors, 'Dates': output_authors})
df.to_csv('data/gizmodo_scrape.csv')