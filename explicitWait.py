from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
#****** Listener class ******
class EventListener(AbstractEventListener):
    def on_exception(self,exception,wdriver):
        print("exception raised and listener caught **###@@@ ",exception)
        wdriver.get_screenshot_as_file("error_screenshot.png")
        wdriver.close()

plain_driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver=EventFiringWebDriver(plain_driver,EventListener())
driver.get("https://www.expedia.com/")
time.sleep(5)
#driver.implicitly_wait(5)
driver.maximize_window()
try:
    if driver.find_element(By.ID,"tab-flight-tab-hp").is_displayed():
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
    else:
        driver.find_element(By.XPATH,"//li/a[@aria-controls='wizard-flight-pwa'").click()
except:
    print("exception in identifying object")

driver.find_element(By.ID,"flight-origin-hp-flight").send_keys("CHI")
driver.find_element(By.ID,"flight-destination-hp-flight").send_keys("NYC")
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys("07/15/2020")
driver.find_element(By.ID,"flight-departing-hp-flight").send_keys(Keys.RETURN)
#driver.find_element(By.ID,"flight-returning-hp-flight").send_keys(" ")
#driver.find_element(By.ID,"flight-returning-hp-flight").send_keys("07/20/2020")
wait=WebDriverWait(driver,20)
ele="//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button"
#wait.until(EC.element_to_be_clickable((By.XPATH, ele)))
#driver.find_element(By.XPATH,ele).click()

ele1=wait.until(EC.element_to_be_clickable((By.ID, 'stopFilter_stops-0')))
# wait.until(EC.element_to_be_clickable((By.XPATH, searchbtn)))
ele1.click()


time.sleep(5)

driver.quit()




