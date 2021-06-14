from splinter import Browser
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


def scrape():

    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    output_dict = {}

    # Mars news_title and story
    mars_url = "https://redplanetscience.com/"
    browser.visit(mars_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    latest_titles = soup.find_all("div", class_ = "content_title")
    new_title = latest_titles[0].text
    latest_p = soup.find_all("div", class_ = "article_teaser_body")
    news_p = latest_p[0].text

    output_dict["title"] = new_title
    output_dict["news"] = news_p

    # Scrape featured image
    pic_url = "https://spaceimages-mars.com/#"
    browser.visit(pic_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    test = soup.find_all("img", class_ ="headerimage fade-in")
    url_end = test[0]["src"]
    feature_image_url = f"https://spaceimages-mars.com/{url_end}"

    output_dict["image"] = feature_image_url


    # Scrape table
    space_url = 'https://galaxyfacts-mars.com/'
    easy_table = pd.read_html(space_url, header = 0)
    mars_df = easy_table[0]
    mars_df.set_index("Mars - Earth Comparison" , drop = True, inplace = True)
    table_html = mars_df.to_html()
    table_html = table_html.replace('\n', '')

    output_dict["table"] = table_html
 
    # Scrape hemisphere pics

    hemi_url = "https://marshemispheres.com/"
    browser.visit(hemi_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    descriptions = soup.find_all("div", class_ = "description")
    images = soup.find_all("img", class_ = "thumb")

    pic_names = []

    for j in range(len(descriptions)):
        pic_names.append(descriptions[j].h3.text.strip())

    urls = []

    for pic in range(len(images)):
        urls.append(images[pic]["src"])

    urls_final = []

    for url in range(len(urls)):
        urls_final.append(f"https://marshemispheres.com/{urls[url]}")

    hemi = [None] * 4 

    for k in range(len(pic_names)):
        hemi[k] = {"title":pic_names[k], "img_url":urls_final[k]}
    
    output_dict["hemi"] = hemi

    browser.quit()

    return output_dict
