# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# %%
# setup splinter
def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

# %% [markdown]
# ## Mars News

# %%
# visit site
url = "https://redplanetscience.com/"
browser.visit(url)


# %%
# bring in soup
html = browser.html
soup = bs(html, 'html.parser')


# %%
# scrape title
news_title = soup.find_all('div', {'class':'content_title'})
news_title[0]


# %%
# clean up title
news_title[0].text


# %%
# scrape paragraph text
news_p = soup.find_all('div', {'class':'article_teaser_body'})
news_p[0]


# %%
# clean up paragraph
news_p[0].text

# %% [markdown]
# ## JPL Mars Space Images - Featured Image

# %%
# path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# %%
# visit site
url = "https://spaceimages-mars.com/"
browser.visit(url)


# %%
featured_image_url='https://spaceimages-mars.com/image/featured/mars2.jpg'

# %% [markdown]
# ## Mars Facts

# %%
# pandas scrape of Mars Facts
url='https://galaxyfacts-mars.com/'


# %%
tables_df=pd.read_html(url)
tables_df


# %%
tables_df=tables[0]
tables_df.head()


# %%
tables_df.to_html('mars.html')

# %% [markdown]
# ## Mars Hemispheres

# %%
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/b3c7c6c9138f57b4756be9b9c43e3a48_valles_marineris_enhanced.tif_full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/f5e372a36edfa389625da6d0cc25d905_cerberus_enhanced.tif_full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/3778f7b43bbbc89d6e3cfabb3613ba93_schiaparelli_enhanced.tif_full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/555e6403a6ddd7ba16ddb0e471cadcf7_syrtis_major_enhanced.tif_full.jpg"},
]


