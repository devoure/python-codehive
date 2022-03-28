#! python
'''
This is a python script to download images from pinterest
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# User input for recipient, subject, and body of the email as well as login information
categorie = input('Enter a category of an image you want?\n')

browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(30)
browser.get('https://www.flickr.com/')
try:
    searchelem = browser.find_element(by=By.TAGNAME, value='input')
    searchelem.send_keys(categorie)
except:
    print('Failed')


