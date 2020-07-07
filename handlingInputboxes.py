import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path='C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe')
driver.get("http://fs2.formsite.com/meherpavan/form2/index.html?")
driver.maximize_window()
tefields=driver.find_elements(By.CLASS_NAME,"text_field")
print("No.of text fields avaialable: ",len(tefields))
firstnm_txt=driver.find_element_by_id("RESULT_TextField-1")
wait=WebDriverWait(driver,10)
wait.until(ec.visibility_of((firstnm_txt)))
print("first name display status is :",firstnm_txt.is_displayed())
if firstnm_txt.is_enabled():
    firstnm_txt.send_keys("abc")

time.sleep(5)
driver.close()
