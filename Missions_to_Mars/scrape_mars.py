# setup and import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path={"executable_path":ChromeDriverManager().install()}
    return Browser("chrome",**executable_path,headless=False)

def scrape_info():
    browser=init_browser()
    # NASA Mars News
    # connect to url
    url="https://mars.nasa.gov/news/"
    browser.visit(url)
    sleep(1)
    # use BeautifulSoup to get latest news title and paragraph text
    html=browser.html
    soup=bs(html,"html.parser")
    result=soup.find("li",class_="slide")
    for r in result:
        news_title=r.find("div",class_="content_title").text.strip()
        news_p=r.find("div",class_="rollover_description_inner").text.strip()
    # JPL Mars Space Images
    # connect to url
    url="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    sleep(1)
    # use BeautifulSoup to get featured image
    html=browser.html
    soup=bs(html,"html.parser")
    base_url=soup.find("a",id="jpl_logo")["href"]
    img_url=soup.find("a",id="full_image")["data-fancybox-href"]
    featured_image_url="https:"+base_url+img_url[1:]
    # Mars Facts
    # set url
    url="https://space-facts.com/mars/"
    # get table
    tables=pd.read_html(url)
    table=tables[0]
    table.columns=['Description','Mars']
    table.set_index('Description',inplace=True)
    # convert pandas dataframe to html table + remove pandas dataframe class in html table
    html_table=table.to_html()
    html_table=html_table.replace('<table border="1" class="dataframe">','<table class="table table-striped">')
    html_table=html_table.replace('text-align: right','text-align: left')
    # Mars Hemisphere
    # connect to url
    url="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    sleep(1)
    # get hemisphere title and link to each hemisphere
    title=[]
    hemi_url=[]
    html=browser.html
    soup = bs(html,"html.parser")
    hemi=soup.find_all("div",class_="description")
    for h in hemi:
        title.append(h.a.h3.text)
        hemi_url.append("https://astrogeology.usgs.gov"+h.a["href"])
    # visit hemisphere url to obtaine image url
    img_url=[]
    for url in hemi_url:
        browser.visit(url)
        html=browser.html
        soup = bs(html,'html.parser')
        for link in soup.find_all("a"):
            if link.text=="Sample":
                img_url.append(link["href"])
    # create a list containing dictionary for each hemisphere
    hemisphere_image_urls=[]
    for i in range(4):
        title_short=title[i].replace(" Enhanced","") # clean up title
        hemisphere_image_urls.append({"title":title_short,"img_url":img_url[i]})
    # quit browser
    browser.quit()
    # return results
    mars_data={
        "mars_news_title":news_title,
        "mars_news_p":news_p,
        "mars_feature_image":featured_image_url,
        "mars_facts_table":html_table,
        "mars_hemi_url":hemisphere_image_urls
    }
    return mars_data
    