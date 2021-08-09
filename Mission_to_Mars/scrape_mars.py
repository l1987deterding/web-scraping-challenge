from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit site
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the title
    article_title = soup.find_all('div', {'class':'content_title'})[0].text

    # Get the article paragraph
    news_p = soup.find_all('div', {'class':'article_teaser_body'})[0].text

    # Get the Mars image
    # visit site
    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    featured_image_url='https://spaceimages-mars.com/image/featured/mars2.jpg'

    # Mars hemispheres images
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
    ]


    # Store data in a dictionary
    mars_data = {
        "featured_img": featured_image_url,
        "article head": article_title,
        "article body": news_p,
        "hemisphere_images": hemisphere_image_urls,   
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data

print(scrape_info())
