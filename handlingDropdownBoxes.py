import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

drp=Select(driver.find_element_by_id("RESULT_RadioButton-9"))
print(" number of items in the dropdown is : ",len(drp.options))
countvar=1
for i in drp.options:
    print(countvar," . ",i.text)
    countvar+=countvar

drp.select_by_index(1)
time.sleep(5)
drp.select_by_value("Radio-1")
time.sleep(5)
drp.select_by_visible_text("Evening")
time.sleep(5)
driver.quit()

