import unittest
from selenium import webdriver

def setUpModule():
    print("This is setUpModule, will be executed once before all the classes")
def tearDownModule():
    print("This is tearDownModule, will be executed after all the classes/modules")

class Testcase2(unittest.TestCase):
    def setUpClass(cls) -> None:
        print("This is setUpClass from Testcase2")

    def tearDownClass(cls) -> None:
        print("This is tearDownClass from TestCase2")

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("This is seUpClass method, which will execute once before the class")
        cls.driver = webdriver.Chrome(
            executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")

    @classmethod
    def setUp(cls) -> None:
        print(" This is setUp method which will be executed before every method in the class")
        #cls.driver.maximizeWindow()

    def test_googlePage(self):
        self.driver.get("http://google.com")
        print("titile of the page is : ", self.driver.title)

    def test_bingPage(self):
        self.driver.get("http://bing.com")
        print("title of the page is :", self.driver.title)

    @classmethod
    def tearDown(cls) -> None:
        print(" This is tearDown method which will be executed after every method in the class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("This is tearDownClass method,which will execute once after all the methods were executed in the class")
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
