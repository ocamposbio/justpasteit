from selenium import webdriver
from time import sleep
import os
import re
import os

_src = "/home/otavio/Desktop/Projects/juspasteit/"
_ext = ".png"

myfile = open("200.txt", "r")

url = myfile.readline()

while url:
    url = myfile.readline() 

    driver = webdriver.Firefox()
    driver.get(url)
    sleep(1)

    driver.get_screenshot_as_file("printou.png")
    driver.quit()
    print("This was: " + url)


myfile.close()