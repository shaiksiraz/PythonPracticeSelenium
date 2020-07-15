import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
    def test_googlePage(self):
        self.driver.get("http://google.com")
        print("titile of the page is : ",self.driver.title)

    def test_bingPage(self):
        self.driver.get("http://bing.com")
        print("title of the page is :",self.driver.title)

    @classmethod
    def test_teardown(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()
