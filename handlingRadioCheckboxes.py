import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager



class EventListener(AbstractEventListener):
    def on_exception(self, exception, driver1):
        print("**** ",exception,"*****")
        driver1.quit

def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    print("in highlight method")
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(.3)
    apply_style(original_style)


plain_driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

#plain_driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
driver=EventFiringWebDriver(plain_driver, EventListener())
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
time.sleep(2)
male_radio=driver.find_element_by_id("RESULT_RadioButton-7_0")
print("Is Male radio button  selected or not :",male_radio.is_selected())
print("Is Male radio button  visible or not :",male_radio.is_displayed())
time.sleep(2)
wait=WebDriverWait(driver,10)
#wait.until(expected_conditions.element_to_be_clickable(male_radio))
if male_radio.is_selected():
    print("radio button is already selected")
else:
    print("radio button is NOT selected")
    highlight(male_radio)
    #male_radio.click()
    driver.execute_script("arguments[0].click();", male_radio)
    time.sleep(5)
print("Is Male radio button  visible or not :",male_radio.is_displayed())
print("Is Male radio button  selected or not :",male_radio.is_selected())

print(len(driver.find_elements_by_class_name('multiple_choice')))
#driver.find_element_by_id("RESULT_CheckBox-8_0").click()
chkbox=driver.find_element_by_xpath("//table[@class='inline_grid choices']//input[@id='RESULT_CheckBox-8_0']")
highlight(chkbox)
driver.execute_script("arguments[0].click();", chkbox)
chkbox.click()
time.sleep(5)
driver.quit()