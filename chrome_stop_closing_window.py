###################
# Chrome webdriver
###################
# D:\app\Python\Python311\Scripts>chromedriver.exe -version
# ChromeDriver 111.0.5563.64 (c710e93d5b63b7095afe8c2c17df34408078439d-refs/branch-heads/5563@{#995})

#########################################################
# Note
# This script will stop closing the browser after running.
#########################################################
from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = options)
driver.get ("http://www.google.com")
