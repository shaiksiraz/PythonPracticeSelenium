from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver.get("http://demo.automationtesting.in")
driver.get_screenshot_as_file("testScreenshot.png") # only .png file can be saved
driver.save_screenshot("testScreenshot.jpg")


driver.quit()