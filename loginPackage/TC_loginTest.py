import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("login by Email")
    def test_loginbyFacebook(self):
        print("login by Facebook")

    def test_loginbyTwitter(self):
        print("login by twitter")

if __name__ == "__main__":
    unittest.main()
