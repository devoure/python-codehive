#! python
'''
This is a python script to auto send emails from the command  line
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# User input for recipient, subject, and body of the email as well as login information
email_name = input('What is your username?\n')
email_password = input('What is your password?\n')
email_recipient = input('Who would you like to send an email to?\n')
email_subject = input('What is the subject of the email?\n')
email_body = input('What would you like to say?\n')


browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(30)
browser.get('http://mail.google.com')
try:
    login_elem  = browser.find_element(by=By.ID, value='identifierId')
    login_elem.send_keys(email_name)
    login_elem = browser.find_element(by=By.ID, value='identifierNext')
    login_elem.click()

    time.sleep(3)
    password_elem = browser.find_element(by=By.NAME, value='password')
    password_elem.send_keys(email_password)
    pw_next_elem = browser.find_element(by=By.ID, value='passwordNext')
    pw_next_elem.click()

    time.sleep(3)
except:
    print('Wrong login credentials')

html_elem = browser.find_element(by=By.TAG_NAME, value='html')
html_elem.send_keys('c')
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_recipient)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_subject)
html_elem.send_keys(Keys.TAB)
html_elem.send_keys(email_body)
html_elem.send_keys(Keys.ENTER)

print('Email was sent.')



