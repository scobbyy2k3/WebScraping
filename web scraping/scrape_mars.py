import pandas as pd
import requests
import os
from bs4 import BeautifulSoup
from splinter import Browser

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

def  scrape (browser):    
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        html = browser.html

        # Retrieve page with the requests module
        # response = requests.get(url)

        # Create BeautifulSoup object; parse with 'lxml'
        soup = BeautifulSoup(html, 'html.parser')

        news_title = soup.find_all('li', class_='slide')
        for result in news_title:
            title = result.find('div', class_='content_title').text
            news_p = result.find('div', class_='article_teaser_body').text
            
            print('-----------------')
            print(title)
            print(news_p)
            
            
            try:
                browser.click_link_by_partial_text('next')
                
            except:
                print("Scraping Complete")

        # JPL Mars Space Images
def  Mars_Space (browser):     

        image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

        browser.visit(image_url)
        # full image
        browser.click_link_by_partial_text('FULL IMAGE')

        response = requests.get(image_url)

        image_html = browser.html


        image_soup = BeautifulSoup(image_html, 'html.parser')

        img_link = image_soup.find("img", class_="thumb")["src"]
        image_path = f'https://www.jpl.nasa.gov{img_link}'
        print(image_path)


        # MARS WEATHER

def  MARS_WEATHER (browser):  

        twitter_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(twitter_url)
        weather_html = browser.html

        # Retrieve page with the requests module
        response = requests.get(twitter_url)

        # Create BeautifulSoup object; parse with 'lxml'
        soup = BeautifulSoup(weather_html, 'html.parser')

        mars = soup.find('div', class_='content') 
        mars_weather = mars.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
        print(mars_weather)

        ### Mars Hemispheres

        # Visit Mars facts url 
def  MARS_Facts (browser): 

        mars_url = 'https://space-facts.com/mars/'

        # Extracting Data
        tables = pd.read_html(mars_url)
        mars_df = tables[1]

        # Dataframe
        mars_df.columns = ['Type', 'Value']
        mars_df

        #Mars Hemispheres

def  MARS_Hemispheres (browser):    

        astro_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(astro_url)

        astro_html = browser.html
        hemi_soup = BeautifulSoup(astro_html, 'html.parser')
        hemi_links= hemi_soup.find_all('div', class_='item')
        hemispheres_url = 'https://astrogeology.usgs.gov'

        for result in hemi_links:
            title = result.find("h3").text
            img_url= result.find("img", class_="thumb")["src"]

            print('-----------------')
            print({"title": title, "img_url": hemispheres_url + img_url})
            