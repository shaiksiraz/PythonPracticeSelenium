import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory": "c:\donwloadedfiles"})
driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe",options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
driver.find_element_by_id("textbox").send_keys("Hi there!")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()
driver.find_element_by_id("pdfbox").send_keys("This is pdf file!")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()

time.sleep(4)
driver.quit()



