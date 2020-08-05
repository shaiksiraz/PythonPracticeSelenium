import unittest

class SignupTest(unittest.TestCase):
    def test_SignupbyEmail(self):
        print("Signup by Email")
    def test_SignupbyFacebook(self):
        print("Signup by Facebook")

    def test_SignupbyTwitter(self):
        print("Signup by twitter")

if __name__ == "__main__":
    unittest.main()
