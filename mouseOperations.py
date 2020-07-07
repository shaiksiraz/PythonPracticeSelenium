import time

from selenium import webdriver
from selenium.webdriver import ActionChains

from highlightObject import highlight

driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element_by_id("txtUsername").send_keys("admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

admin=driver.find_element_by_xpath("//a[@id='menu_admin_viewAdminModule']/b")
usermgtmnu=driver.find_element_by_id("menu_admin_UserManagement")
usersmnu=driver.find_element_by_id("menu_admin_viewSystemUsers")

actions=ActionChains(driver)
actions.move_to_element(admin).perform()
time.sleep(1)
actions.move_to_element(usermgtmnu).perform()
time.sleep(1)
actions.move_to_element(usersmnu).perform()
time.sleep(1)
usersmnu.click()
#****** we can combine all the above actions in single line
#actions.move_to_element(admin).move_to_element(usermgtmnu).move_to_element(usersmnu).click().perform()

time.sleep(5)


#******* double click operations **********
driver.get("http://testautomationpractice.blogspot.com/")
copybtn=driver.find_element_by_xpath("//div[@id='HTML10']//button[text()='Copy Text']")

driver.execute_script("arguments[0].scrollIntoView();",copybtn)
highlight(copybtn)
actions=ActionChains(driver)


actions.double_click(copybtn).perform()
time.sleep(5)



driver.close()

