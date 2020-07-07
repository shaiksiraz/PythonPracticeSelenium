import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from highlightObject import highlight

driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
elebtn=driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral' and text()='right click me']")
highlight(elebtn)
actions=ActionChains(driver)
actions.move_to_element(elebtn).context_click().send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)

driver.quit()