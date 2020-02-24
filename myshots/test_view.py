from django.test import TestCase
# import pytest
import unittest

import time
from selenium import webdriver


def shot_func_test():
    DRIVER = 'chromedriver'
    driver = webdriver.Chrome(DRIVER)
    URL = 'http://www.webcenter4u.com'
    driver.get(URL)

    while URL:
        myimg = 'myscreen1.png'
        screenshot = driver.save_screenshot('../media/myscreens/'+myimg)
        time.sleep(5)
    driver.quit()
    return


shot_func_test()
