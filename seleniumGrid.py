import time

from selenium import webdriver

driver = webdriver.Remote(command_executor="http://192.168.0.15:4444/wd/hub",
        desired_capabilities={
            "browserName": "chrome",
            "platform": "WIN10",
            "platformName": "windows",
            'javascriptEnabled': True
        })

driver.get("http://google.com")
time.sleep(2)
driver.quit()