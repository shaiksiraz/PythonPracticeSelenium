import time
from selenium import webdriver
from highlightObject import highlight

driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")


ele1=driver.find_element_by_xpath("//div[@id='Tabbed']/a/button")
highlight(ele1)
ele1.click()
whandle=driver.window_handles

for i in whandle:
    print("** window title is ** ",i.title())
    driver.switch_to.window(i)
    print(" browser titile is : ",driver.title)
    if driver.title=="Sakinalium | Home":
        driver.close()
driver.switch_to.window(whandle[0])
#driver.get_window_position("Cdwindow-94083972Dda002E6C781A37B3B81496B")
chandle=driver.current_window_handle
print("current window active is : ",chandle)

time.sleep(5)
driver.quit()