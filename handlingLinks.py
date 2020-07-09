import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
all_links=driver.find_elements_by_tag_name("a")
print("No.of Links in he webpage is :",len(all_links))
for i in all_links:
    print(i.text)

driver.find_element(By.LINK_TEXT,"REGISTER").click()
time.sleep(5)
driver.back()
driver.find_element(By.PARTIAL_LINK_TEXT,"REG")
time.sleep(5)

driver.quit()