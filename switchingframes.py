import time
from highlightObject import highlight
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver.get("https://seleniumhq.github.io/selenium/docs/api/java/index.html")
time.sleep(5)
driver.switch_to.frame("packageListFrame")
ele1=driver.find_element_by_link_text("org.openqa.selenium")
highlight(ele1)
ele1.click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
ele2=driver.find_element_by_link_text("com.thoughtworks.selenium")
highlight(ele2)
ele2.click()

ele3=driver.find_element_by_xpath("//table[@class='typeSummary']//td[@class='colFirst']/a[text()='SeleniumException']")
highlight(ele3)
ele3.click()
time.sleep(3)
driver.get_screenshot_as_file("screenshot.png")
driver.quit()

