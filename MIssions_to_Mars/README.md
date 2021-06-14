Repository for the Georgia Tech Data Science and Analytics: web-scraping-challenge.

In this excercise we used 'BeautifulSoup', 'splinter', and 'flask'in Python with Jupyter Notebook to scrape data about Mars from various websites.

Data were scraped from the following sites:
  
  * redplanetscience.com  -> latest news title and storey (text).
  * spaceimages-mars.com -> image of the day
  * galaxyfacts-mars.com -> comparsion table of Earth and Mars
  * marshemispheres.com -> pictures of the four hemispheres of Mars

Python code for the initial scraping was done in a Jupyter Notebook file and was then turned into a flask app.

Directory structure: web-scraping-challenge/

<strong>/Mission-to-Mars/mission_to_mars.ipynb</strong>   
Prototyping Python code for scraping app with printed outputs

<strong>/Mission-to-Mars/templates/index.html</strong>     
HTML file with Bootstrap CSS styling for webpage

<strong>/Mission-to-Mars/screenshots/screenshot_1</strong>   
Upper screenshot of webpage

<strong>/Mission-to-Mars/screenshots/screenshot_2</strong>   
Lower screenshot of webpage

<strong>/Mission-to-Mars/app.py</strong>  
Flask app code

<strong>/Mission-to-Mars/scrap_mars.py</strong>   
Python code scraping code called by /scrape route in app.py 

All code was written by Corey Devin Anderson
