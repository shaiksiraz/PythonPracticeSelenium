from selenium import webdriver
import unittest

class assertsTests(unittest.TestCase):
    def test_checkgoogle(self):
        driver=webdriver.Chrome(executable_path="C:/Users/shaik/PycharmProjects/drivers/chromedriver_win32/chromedriver.exe")
        driver.get("http://www.google.com")
        title=driver.title
        #self.assertEqual("Google123",title,"expected page title is not matched")
        #self.assertNotEqual("Google", title, "expecting page title should not match")
        #self.assertTrue("Google"==title, "expecting page title should match")
        self.assertFalse("Google12233" == title, "expecting page title should not match")
        self.assertIsNotNone(driver, "checking driver is NOT none")
        driver=None
        self.assertIsNone(driver,"checking driver is none")
        list=("python","java","vbscript","ruby")
        self.assertIn("python",list,"checking the list item exist")
        self.assertNotIn("python123", list, "checking the list item NOT exist")

        self.assertGreater(100,50)
        self.assertGreater("Hi", "Hello")
        self.assertGreaterEqual(100,100)
        self.assertGreaterEqual("hi", "Hi")
        self.assertLess(100,200)
        self.assertLessEqual(100,100)


if __name__ == "__main__" :
    unittest.main()