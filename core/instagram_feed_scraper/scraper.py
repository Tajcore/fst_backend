
import os, sys
import urllib.request
import time
from selenium import webdriver
from datetime import datetime

from ..models import NewsFeedImage, NewsFeed



# Path to Static folder
img_Dir = "../../static/images/news_feed_images"  

# Initializing webdriver for firefox and link to the FST Guild Page
driver = webdriver.Firefox()
driver.get("https://www.instagram.com/fst_uwimona/")

python_button = driver.find_element_by_xpath(
    "/html/body/div[1]/section/main/div/div[3]/div[1]/div/button")
python_button.click()


# Scroll Down function to dynamically load all posts on the page
def scroll_down(driver):
    """A method for scrolling the page."""

    # Get scroll height.
    last_height = driver.execute_script(
        "return document.body.scrollHeight")

    while True:

        # Scroll down to the bottom.
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load the page.
        time.sleep(2)

        # Calculate new scroll height and compare with last scroll height.
        new_height = driver.execute_script(
            "return document.body.scrollHeight")

        if new_height == last_height:

            break

        last_height = new_height



# Main scraping function body
scroll_down(driver)
posts = []

links = driver.find_elements_by_tag_name('a')

for link in links:
    post = link.get_attribute("href")
    if '/p/' in post:
        posts.append(post)

for post in posts:
    driver.get(post)
   
    shortcode = driver.current_url.split("/")[-2]
    
   
    filepath = os.path.join(img_Dir, shortcode + ".jpg")
    description = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/span").text
    title = "FST Updates"
    date = driver.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div/article/div[3]/div[2]/a/time").text
    converted_date = datetime.strptime(date, '%B %d, %Y')

    type = driver.find_element_by_xpath(
        '//meta[@property="og:type"]').get_attribute("content")

    if type == "instapp:photo":
        download_url = driver.find_element_by_xpath(
            '//meta[@property="og:image"]').get_attribute("content")
       
        urllib.request.urlretrieve(
            download_url, filepath)
        print("""
        URL: {}
        Date: {}
        Title: {}
        Description: {}
        ImageURL: {}""".format(post,converted_date,title,description,download_url))
  