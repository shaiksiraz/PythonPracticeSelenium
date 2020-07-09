import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
ele1=driver.find_element_by_id("box4")
ele2=driver.find_element_by_id("box106")
actions=ActionChains(driver)
actions.drag_and_drop(ele1,ele2).perform()
time.sleep(4)
driver.quit()

