# web-scraping-challenge

Completed web scraping (week 12) homework for Monash University Data Analytics Boot Camp.

Goal is to build a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

Folder structure include - 
* ***Mission_to_Mars*** folder containing
    * ***mission_to_mars.ipynb***  - jupyter notebook containing scraping tasks, ie.
        * scrape *[NASA Mars News Site](https://mars.nasa.gov/news/)* for latest news title and paragraph text
        * scrape *[JPL](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars)* for its featured space image
        * scrape the *[Mars Facts](https://space-facts.com/mars/)* webpage for facts on Mars
        * scrape the *[USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars)* for high resolution images of Mars' hemispheres
    * ***scrape_mars.py*** - script to scrape the above sites for the relevant data
    * ***app.py*** - Flask API to launch html file for Mission to Mars
    * ***static*** folder containing css stylesheet for HTML page
    * ***templates*** folder containing template *index.html* file