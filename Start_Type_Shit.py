from web_driver import *
import time
from Password import *

while True:
    driver.get("https://laketravis.schoology.com/apps/364888653/run/course/6787633448")
    username_box = driver.find_element(By.ID, 'edit-mail')
    password_box = driver.find_element(By.ID, 'edit-pass')
    driver.find_element(By.ID, 'edit-mail').send_keys(username)
    time.sleep(2000)
    username_box.send_keys(password)
    time.sleep(2000)
    driver.find_element(By.ID, 'edit-submit').click
    time.sleep(2000)
    driver.get("https://lthslatin.org")
    time.sleep(3000)
