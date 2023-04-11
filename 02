from selenium import webdriver
from selenium.webdriver.common.by import By

def test_selenium_demo():
  options = webdriver.ChromeOptions()
  options.add_experimental_option("detach", True)

  driver = webdriver.Chrome(options=options)
  driver.get ("http://www.google.com")
  element = driver.find_element(By.ID, "email")
  element.clear()
  element.send_keys("Test@gmail.com")

  element_pass = driver.find_element(By.ID, "pass")
  element_pass.clear()
  element_pass.send_keys("Pssword")

  login_button_element = driver.find_element(By.NAME, "login")
  login_button_element.click()
#driver = webdriver.Chrome("D:\app\Python\Python311\Scripts\chromedriver.exe")

test_selenium_demo()
