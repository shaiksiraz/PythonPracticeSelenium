import time

import highlightObject
from highlightObject import highlight
from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    time.sleep(2)
    highlight(driver.find_element_by_xpath("//div[@id='HTML9']"))
    highlight(driver.find_element_by_xpath("//div[@id='HTML9']//div"))
    clickbtn = driver.find_element(By.XPATH,"//div[@id='HTML9']//div[@class='widget-content']//button")
    highlight(clickbtn)
    clickbtn.click()
    driver.switch_to.alert().accept()
    time.sleep(5)
    clickbtn.click()
    driver.switch_to.alert().dismiss()
    time.sleep(5)
finally:
    driver.quit()