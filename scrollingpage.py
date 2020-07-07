import time

from selenium import webdriver

from highlightObject import highlight

driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.execute_script("window.scrollBy(0,1000)","")
print("page scrolled by 1000 pixel")
time.sleep(2)

ele1=driver.find_element_by_link_text("Salon Travel")
highlight(ele1)
driver.execute_script("window.scrollBy(0,-1000)","") # to scroll back to top
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView();",ele1)
print(" page was scrolled until find the expected object")
time.sleep(2)
driver.execute_script("window.scrollBy(0,-(document.body.scrollHeight))","") # to scroll back to top
time.sleep(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","") # to scroll till end of the page
time.sleep(2)
print("page was scrolled until end of the page")
driver.quit()