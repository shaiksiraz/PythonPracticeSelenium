import unittest
from loginPackage.TC_loginTest import LoginTest
from loginPackage.TC_signupTest import SignupTest

from paymentPackage.TC_Payment import PaymentTest
from paymentPackage.TC_paymentReturn import PaymentReturn

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturn)

sanitySuite=unittest.TestSuite([tc1,tc2])
functionalTestSuite=unittest.TestSuite([tc3,tc4])
masterTestSuite=unittest.TestSuite([tc1,tc2,tc3,tc4])

#unittest.TextTestRunner().run(sanitySuite)
#unittest.TextTestRunner().run(functionalTestSuite)
unittest.TextTestRunner().run(masterTestSuite)


