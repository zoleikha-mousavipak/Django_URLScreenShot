from django.shortcuts import render,redirect
import time
from selenium import webdriver
# from .models import *


def shot_func():
    DRIVER = 'chromedriver'
    driver = webdriver.Chrome(DRIVER)
    URL = 'http://www.webcenter4u.com'
    driver.get(URL)

    x = 0
    while URL:
        x += 1
        myimg = 'myscreen' + str(x) + '.png'
        screenshot = driver.save_screenshot('../media/myscreens/'+myimg)

        # 1 per second is about 1000 per month
        time.sleep(1)

        # create a file to collect images
        myfile = open('../media/myscreens.txt','a')
        myfile.write(str(myimg)+"\n")
        myfile.close()

        # add to databse
        # myinstance = MyScreen(img=myimg)
        # myinstance.save()

    driver.quit()
    return



shot_func()


