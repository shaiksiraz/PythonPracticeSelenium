import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame("frame-one1434677811")
eleupload=driver.find_element_by_id("RESULT_FileUpload-10")
eleupload.send_keys("C:/Users/shaik/OneDrive/Desktop/oracleDetils.txt")
time.sleep(4)
driver.quit()

