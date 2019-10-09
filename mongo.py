#dependecies
from bs4 import BeautifulSoup as bs
# from splinter import browser
import pandas as pd
import requests
import pymongo

#define pymongo to work with mongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

#define db & collection(table)
db = client.happiness_db
collection = happiness_database.website

#url to scrape, pull pg with get request, create bs object & parse
# url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
# response = requests.get(url)
# soup = bs(response.text, 'html.parser')

# #pull title text in variable & print
# news_title = soup.title.text.strip()

# #pull paragraph as variable & print
# news_paragraph = soup.body.p.text


# #new twitter scrape for weather tweet
# t_url = "https://twitter.com/marswxreport?lang=en"
# response = requests.get(t_url)
# soup = bs(response.text, 'html.parser')

# #print first relevant result
# mars_weather = soup.find_all('p')[4].text

# #scrape tabular data with pandas.read_html
# facts_url = "https://space-facts.com/mars/"
# tables = pd.read_html(facts_url)
# type(tables)

renamed.to_html

hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
response = requests.get(hemi_url)
soup = bs(response.text, 'html.parser')

hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/04085d99ec3713883a9a57f42be9c725_valles_marineris_enhanced.tif_thumb.png"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/dfaf3849e74bf973b59eb50dab52b583_cerberus_enhanced.tif_thumb.png"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/7677c0a006b83871b5a2f66985ab5857_schiaparelli_enhanced.tif_thumb.png"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astrogeology.usgs.gov/cache/images/aae41197e40d6d4f3ea557f8cfe51d15_syrtis_major_enhanced.tif_thumb.png"},
]
scrape = {"mars_title": news_title, 
    "mars_article": news_paragraph,
    "weather": mars_weather,
    "mars_data": df,
    "hemispheres": hemisphere_image_urls}
print(scrape)




