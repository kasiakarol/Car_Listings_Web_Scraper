from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import time

url = 'https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'
df = pd.DataFrame(columns=['Link', 'Title', 'Price', 'Colour'])  # Creating DataFrame with specified columns
page_num = 1
max_page = 5  # Scraping only 5 first pages, number be adjusted by a user
data = []  # Empty list to collect the data

while page_num <= max_page:  # Loop through each page to scrape data until the maximum page limit is reached
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    posts = soup.find_all('div', class_='t-flex t-gap-6 t-items-start t-p-6')

    # Getting url, title, price and colour of each car posted
    for post in posts:
        try:
            link = 'https://www.carpages.ca' + post.find('a', class_='t-flex t-items-start t-w-[130px] t-shrink-0').get('href')
        except AttributeError:
            link = 'Link is not available.'

        try:
            title = post.find('h4', class_='hN').find('a').get('title')
        except AttributeError:
            title = 'Title is not available'

        try:
            price = post.find('span', class_=re.compile('t-font-bold t-text-xl')).text.strip()
        except AttributeError:
            price = 'Price is not available'

        try:
            colour = post.find('span', class_='t-text-sm t-font-bold').text.strip()
        except AttributeError:
            colour = 'Colour is not available'

        # Collecting all the posts in a list that will be later on added to the dataframe
        data.append({'Link': link, 'Title': title, 'Price': price, 'Colour': colour})

    # Incrementing page numer track the maximum number of pages scraped
    page_num += 1

    # Searching for the next page link if available
    next_page = soup.find('a', class_='nextprev')
    if next_page:
        next_page_full = 'https://www.carpages.ca' + next_page.get('href')
        url = next_page_full
    else:
        break

    time.sleep(1)  # Adding a delay to prevent overloading the server

df = pd.DataFrame(data)

df.index = df.index + 1  # Adjusting index to start from 1 for better readability

# Saving data frame as csv file
output_file_path = 'cars_scraper.csv'  # Path can be adjusted by the user
df.to_csv(output_file_path)
