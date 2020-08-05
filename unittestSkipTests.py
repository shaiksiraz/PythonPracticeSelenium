import unittest
class skipTests(unittest.TestCase):
    globalVar=0
    @unittest.SkipTest
    def test_search(self):
        print("This is search test")
    @unittest.skip("This method is still under construction!!")
    def test_advancedSearch(self):
        print("This is advanced test")
        globalVar=1

    @unittest.skipIf(globalVar==0,"global variable is not updated so,skipped")
    def test_login(self):
        print("This is login test")

    def test_loginWithGoogle(self):
        print("This is login with Google")

    def test_loginWithTwitter(self):
        print("This is login with Twitter")

    def test_loginwithFacebook(self):
        print("This is login with Facebook")

if __name__ == "__main__" :
    unittest.main()