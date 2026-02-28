
from time import sleep
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select

class TestBankApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        sleep(2)


    def navigate_to_edit_customer(self):
        self.driver.find_element(By.LINK_TEXT, "Edit Customer").click()
        sleep(2)



    def navigate_to_delete_customer(self):
        self.driver.find_element(By.LINK_TEXT, "Delete Customer").click()
        sleep(1)

    def navigate_to_new_account(self):
        self.driver.find_element(By.LINK_TEXT, "New Account").click()
        sleep(1)



    def navigate_to_new_customer(self):
        self.driver.find_element(By.LINK_TEXT, "New Customer").click()
        sleep(2)



    # NC01: Ensure blank customer name shows error
    def test01_customer_name_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_new_customer()
        self.driver.find_element(By.NAME, "name").send_keys(Keys.TAB)
        sleep(1)
        error = self.driver.find_element(By.ID, "message").text
        self.assertEqual(error, "Customer name must not be blank")
        sleep(3)

    # NC02: Ensure numeric customer name shows error
    def test02_customer_name_numeric(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()
        self.driver.find_element(By.NAME, "name").send_keys("1234")
        sleep(1)
        error = self.driver.find_element(By.ID, "message").text
        self.assertEqual(error, "Numbers are not allowed")

    # NC03: Ensure special characters in name shows error
    def test03_customer_name_special_chars(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()
        self.driver.find_element(By.NAME, "name").send_keys("name!@#")
        sleep(1)
        error = self.driver.find_element(By.ID, "message").text
        self.assertEqual(error, "Special characters are not allowed")

    # NC04: Name starting with space shows correct error
    def test04_customer_name_valid(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()
        self.driver.find_element(By.NAME, "name").send_keys(" John Doe")
        sleep(1)
        error = self.driver.find_element(By.ID, "message").text
        self.assertEqual(error, "First character can not have space")



    # NC05: Blank address field should show error
    def test05_address_cannot_be_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "addr").send_keys(Keys.TAB)
        sleep(1)
        error = self.driver.find_element(By.ID, "message3").text
        self.assertEqual(error, "Address Field must not be blank")

    # NC06: Address field starting with space should error
    def test06_address_cannot_have_first_blank_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "addr").send_keys(" Ronald Drive")
        sleep(1)
        error = self.driver.find_element(By.ID, "message3").text
        self.assertEqual(error, "First character can not have space")


    # NC07: Blank city field should show error
    def test07_city_cannot_be_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "city").send_keys(Keys.TAB)
        sleep(1)
        error = self.driver.find_element(By.ID, "message4").text
        self.assertEqual(error, "City Field must be not blank")

    # NC08: Numeric city input should show error
    def test08_city_cannot_be_numeric(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "city").send_keys("1234")
        sleep(1)
        error = self.driver.find_element(By.ID, "message4").text
        self.assertEqual(error, "Numbers are not allowed")

    # NC09: City with special characters shows error
    def test09_city_cannot_have_special_character(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "city").send_keys("City!@#")
        sleep(1)
        error = self.driver.find_element(By.ID, "message4").text
        self.assertEqual(error, "Special characters are not allowed")

    # NC10: City starting with space shows error
    def test10_city_cannot_have_first_blank_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "city").send_keys(" Oshawa")
        sleep(1)
        error = self.driver.find_element(By.ID, "message4").text
        self.assertEqual(error, "First character can not have space")



    # NC11: Blank state field triggers error
    def test11_state_cannot_be_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.navigate_to_new_customer()


        self.driver.find_element(By.NAME, "state").send_keys(Keys.TAB)
        sleep(1)
        error = self.driver.find_element(By.ID, "message5").text
        self.assertEqual(error, "State must not be blank")

    # NC12: Numeric state should show error
    def test12_state_cannot_be_numeric(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.navigate_to_new_customer()
        self.driver.find_element(By.NAME, "state").send_keys("1234")
        sleep(1)
        error = self.driver.find_element(By.ID, "message5").text
        self.assertEqual(error, "Numbers are not allowed")

    # NC13: Special chars in state input should error
    def test13_state_State_cannot_have_special_character(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "state").send_keys("State!@#")
        sleep(1)
        error = self.driver.find_element(By.ID, "message5").text
        self.assertEqual(error, "Special characters are not allowed")

    # NC14: State starting with space should show error
    def test14_state_cannot_have_first_blank_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "state").send_keys(" California")
        sleep(1)
        error = self.driver.find_element(By.ID, "message5").text
        self.assertEqual(error, "First character can not have space")


    # NC15: PIN with characters should show error
    def test15_pin_must_be_numeric(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "pinno").send_keys("1234")
        sleep(1)
        error = self.driver.find_element(By.ID, "message6").text
        self.assertEqual(error, "Characters are not allowed")

    # NC16: Blank PIN should show required error
    def test16_pin_cannot_be_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "pinno").send_keys(Keys.TAB)
        sleep(1)
        error = self.driver.find_element(By.ID, "message6").text
        self.assertEqual(error, "PIN Code must not be blank")

    # NC17: Less than 6 digit PIN should error
    def test17_pin_must_have_six_digits(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "pinno").send_keys("12")
        sleep(1)
        error = self.driver.find_element(By.ID, "message6").text
        self.assertEqual(error, "PIN Code must have 6 Digits")

    # NC18: Special characters in PIN should error
    def test18_pin_cannot_have_special_character(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.navigate_to_new_customer()
        self.driver.find_element(By.NAME, "pinno").send_keys("!@#")
        sleep(1)
        error = self.driver.find_element(By.ID, "message6").text
        self.assertEqual(error, "Special characters are not allowed")

    # NC19: PIN starting with space should show error
    def test19_pin_cannot_have_first_blank_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.navigate_to_new_customer()
        self.driver.find_element(By.NAME, "pinno").send_keys(" 1234")
        sleep(1)
        error = self.driver.find_element(By.ID, "message6").text
        self.assertEqual(error, "First character cannot have space")

    # NC20: Characters in PIN should show error
    def test20_pin_cannot_have_blank_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()
        self.driver.find_element(By.NAME, "pinno").send_keys("A BCD")
        sleep(1)
        error = self.driver.find_element(By.ID, "message6").text
        self.assertEqual(error, "Characters are not allowed")

    # ========== MOBILE TESTS ==========

    # NC21: Blank mobile number should show error
    def test21_mobile_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "telephoneno").send_keys(Keys.TAB)
        sleep(1)
        error = self.driver.find_element(By.ID, "message7").text
        self.assertEqual(error, "Mobile no must not be blank")

    # NC22: Mobile starting with space should error
    def test22_mobile_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "telephoneno").send_keys(" 6471234567")
        sleep(1)
        error = self.driver.find_element(By.ID, "message7").text
        self.assertEqual(error, "First character can not have space")

    # NC23: Mobile with space-separated digits should error
    def test23_mobile_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "telephoneno").send_keys("123 123")
        sleep(1)
        error = self.driver.find_element(By.ID, "message7").text
        self.assertEqual(error, "Characters are not allowed")

    # NC24: Special characters in mobile should error
    def test24_mobile_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "telephoneno").send_keys("886636!@12")
        sleep(1)
        error = self.driver.find_element(By.ID, "message7").text
        self.assertEqual(error, "Special characters are not allowed")


    # NC25: Blank email field should show error
    def test25_email_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        sleep(1)
        error = self.driver.find_element(By.ID, "message9").text
        self.assertEqual(error, "Email ID must not be blank")

    # NC26: Email missing domain ending should show error
    def test26_email_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()
        self.driver.find_element(By.NAME, "emailid").send_keys("guru99@gmail")
        sleep(1)
        error = self.driver.find_element(By.ID, "message9").text
        self.assertEqual(error, "Email-ID is not valid")

    # NC27: Email with leading space should show error
    def test27_email_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()
        self.driver.find_element(By.NAME, "emailid").send_keys(" guru99@gmail")
        sleep(1)
        error = self.driver.find_element(By.ID, "message9").text
        self.assertEqual(error, "Email-ID is not valid")

    # NC28: Blank password field should show error
    def test28_email_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_customer()

        self.driver.find_element(By.NAME, "emailid").send_keys(Keys.TAB)
        sleep(1)
        error = self.driver.find_element(By.ID, "message18").text
        self.assertEqual(error, "Password must not be blank")


    # EC01: Empty Customer ID should trigger required error
    def test29_case_customer_id_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        sleep(1)
        error = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(error, "Customer ID is required")

    # EC02: Customer ID with letters should show error
    def test30_case_customer_id_with_letters(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Acc")
        sleep(1)
        error = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(error, "Characters are not allowed")

    # EC03: Customer ID with symbols shows special char error
    def test31_case_customer_id_with_special_chars(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("!@#")
        sleep(1)
        error = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(error, "Special characters are not allowed")

    # EC04: Valid Customer ID navigates to edit form
    def test32_case_customer_id_valid(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        sleep(1)
        error = self.driver.find_element(By.CLASS_NAME, "heading3").text
        self.assertEqual(error,"Edit Customer Form")

    # EC05: Blank address field triggers required message
    def test33_case_address_field_blank(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        address = self.driver.find_element(By.NAME, "addr")
        address.clear()
        address.send_keys(Keys.TAB)
        error = self.driver.find_element(By.ID, "message3").text
        self.assertEqual(error, "Address Field must be blank")
        sleep(1)

    # EC06: Blank city field triggers required message
    def test34_case_city_field_blank(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        city = self.driver.find_element(By.NAME, "city")
        city.clear()
        city.send_keys(Keys.TAB)
        sleep(1)

        error = self.driver.find_element(By.ID, "message4").text
        self.assertEqual(error, "City Field must not be blank")

    # EC07: City field with numbers shows error
    def test35_city_field_with_numbers(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        city = self.driver.find_element(By.NAME, "city")
        city.clear()
        city.send_keys("1234")
        sleep(1)

        error = self.driver.find_element(By.ID, "message4").text
        self.assertEqual(error, "Numbers are allowed")
        sleep(1)

    # EC08: City field with symbols shows error
    def test36_city_field_with_special_chars(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        city = self.driver.find_element(By.NAME, "city")
        city.clear()
        city.send_keys("!@#")
        sleep(1)

        error = self.driver.find_element(By.ID, "message4").text
        self.assertEqual(error, "Special characters are not allowed")
        sleep(1)

    # EC09: Blank state field triggers required message
    def test37_state_field_blank(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        state = self.driver.find_element(By.NAME, "state")
        state.clear()
        state.send_keys(Keys.TAB)
        sleep(1)

        error = self.driver.find_element(By.ID, "message5").text
        self.assertEqual(error, "State must be blank")
        sleep(1)


    # EC10: State field with numbers shows error
    def test38_state_field_with_numbers(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        state = self.driver.find_element(By.NAME, "state")
        state.clear()
        state.send_keys("1234")
        sleep(1)

        error = self.driver.find_element(By.ID, "message5").text
        self.assertEqual(error, "Numbers are not allowed")
        sleep(1)

    # EC11: State field with special chars shows error
    def test39_state_field_with_special_chars(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        state = self.driver.find_element(By.NAME, "state")
        state.clear()
        state.send_keys("!@#")
        sleep(1)

        error = self.driver.find_element(By.ID, "message5").text
        self.assertEqual(error, "Special characters are not allowed")
        sleep(1)

    # EC12: PIN field with letters shows error
    def test40_pin_with_letters(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        pin = self.driver.find_element(By.NAME, "pinno")
        pin.clear()
        pin.send_keys("1234PIN")
        sleep(1)

        error = self.driver.find_element(By.ID, "message6").text
        self.assertEqual(error, "Characters are not allowed")
        sleep(1)

    # EC13: Blank PIN field shows required error
    def test41_pin_field_blank(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        pin = self.driver.find_element(By.NAME, "pinno")
        pin.clear()
        pin.send_keys(Keys.TAB)
        sleep(1)

        error = self.driver.find_element(By.ID, "message6").text
        self.assertEqual(error, "PIN Code must not be blank")
        sleep(1)

    # EC14: PIN field with less digits shows error
    def test42_pin_less_than_6_digits(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        pin = self.driver.find_element(By.NAME, "pinno")
        pin.clear()
        pin.send_keys("1234")
        sleep(1)
        error = self.driver.find_element(By.ID, "message6").text
        self.assertEqual(error, "PIN Code must have 6 Digits")

    # EC15: PIN field with symbols shows error
    def test43_pin_with_special_chars(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        pin = self.driver.find_element(By.NAME, "pinno")
        pin.clear()
        pin.send_keys("!@#")
        sleep(1)
        error = self.driver.find_element(By.ID, "message6").text
        self.assertEqual(error, "Special characters are not allowed")

    # EC16: Blank telephone field shows required message
    def test44_telephone_blank(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        mobile = self.driver.find_element(By.NAME, "telephoneno")
        mobile.clear()
        mobile.send_keys(Keys.TAB)
        sleep(1)

        error = self.driver.find_element(By.ID, "message7").text
        self.assertEqual(error, "Telephone no must not be blank")
        sleep(1)

        # EC17: Telephone field with symbols shows error
    def test45_telephone_with_special_chars(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        mobile = self.driver.find_element(By.NAME, "telephoneno")
        mobile.clear()
        mobile.send_keys("886636!@12")
        sleep(1)

        error = self.driver.find_element(By.ID, "message7").text
        self.assertEqual(error, "Special characters are not allowed")
        sleep(1)

        # EC18: Blank email field shows required message
    def test46_email_blank(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        email = self.driver.find_element(By.NAME, "emailid")
        email.clear()
        email.send_keys(Keys.TAB)
        sleep(1)

        error = self.driver.find_element(By.ID, "message9").text
        self.assertEqual(error, "Email-ID must not be blank")
        sleep(1)

        # EC19: Invalid email format should trigger validation
    def test47_email_invalid_format(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        email = self.driver.find_element(By.NAME, "emailid")
        email.clear()
        email.send_keys("guru@web")
        sleep(1)

        error = self.driver.find_element(By.ID, "message9").text
        self.assertEqual(error, "Email-ID is not valid")
        sleep(1)

    # EC20: Submit with blank required fields returns error
    def test48_submit_form_with_blank_fields(self):
        self.driver.get("https://demo.guru99.com/V4/")
        sleep(2)
        self.driver.find_element(By.NAME, "uid").send_keys("mngr618034")
        self.driver.find_element(By.NAME, "password").send_keys("sujUjab")
        self.driver.find_element(By.NAME, "btnLogin").click()
        sleep(2)

        self.navigate_to_edit_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("17459")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)

        submit = self.driver.find_element(By.NAME, "sub")
        submit.click()
        sleep(1)

        error = self.driver.find_element(By.XPATH, "/html/body")

        self.assertTrue(len(error.get_attribute('innerHTML')) != 0, "")

    # DC1
    def test49_empty_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_delete_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("")
        self.driver.find_element(By.NAME, "cusid").send_keys("\t")  # or click outside
        sleep(1)

        message = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(message, "Customer ID can not be blank")
    # DC2
    def test50_non_numeric_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.refresh()
        self.navigate_to_delete_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("Acc123")
        sleep(1)

        message = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(message, "Characters are not allowed")

     # DC3
    def test51_special_character_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_delete_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("123!@#")

        sleep(1)
        message = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(message, "Special characters are not allowed")

     # DC4
    def test52_space_in_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_delete_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")

        sleep(1)
        message = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(message, "Characters are not allowed")

     # DC5
    def test53_first_can_not_be_character_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_delete_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("  ")

        sleep(1)
        message = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(message, "First character cannot have space")

      # DC6
    def test54_invalid_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_delete_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Do you really want to delete this Customer?")
        alert.dismiss()

      # DC7
    def test55_protected_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_delete_customer()
        self.driver.find_element(By.NAME, "cusid").send_keys("75857")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        alert = self.driver.switch_to.alert
        alert.accept()
        sleep(3)
        self.assertEqual(
            "Customer could not be deleted!!. First delete all accounts of this customer then delete the customer",
            alert.text)
        alert = self.driver.switch_to.alert
        alert.accept()
        sleep(3)

    # DC8
    def test56_reset_button(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_delete_customer()
        customer_id_field = self.driver.find_element(By.NAME, "cusid")
        customer_id_field.send_keys("qwer123456")
        self.driver.find_element(By.NAME, "res").click()
        sleep(1)
        self.assertEqual(customer_id_field.get_attribute("value"), "")

      # NA1
    def test57_empty_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_new_account()
        self.driver.find_element(By.NAME, "cusid").send_keys(Keys.TAB)
        sleep(1)
        message = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(message, "Customer ID is required")

       # NA2
    def test58_alpha_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_new_account()
        self.driver.find_element(By.NAME, "cusid").send_keys("1234Ace")
        sleep(1)
        message = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(message, "Characters are not allowed")

     # NA3
    def test59_special_char_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_new_account()
        self.driver.find_element(By.NAME, "cusid").send_keys("123@#")

        sleep(1)
        message = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(message, "Special characters are not allowed")

   # NA4
    def test60_space_in_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.refresh()
        self.navigate_to_new_account()
        self.driver.find_element(By.NAME, "cusid").send_keys("123 12")
        sleep(1)
        message = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(message, "Characters are not allowed")

    # NA5
    def test61_leading_space_in_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_new_account()
        self.driver.find_element(By.NAME, "cusid").send_keys("  ")
        sleep(1)
        message = self.driver.find_element(By.ID, "message14").text
        self.assertEqual(message, "First character cannot have space")

   # NA6
    def test62_empty_deposit(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)


        self.navigate_to_new_account()
        self.driver.find_element(By.NAME, "inideposit").send_keys(Keys.TAB)
        sleep(1)
        message = self.driver.find_element(By.ID, "message19").text
        self.assertEqual(message, "Initial Deposit must not be blank")

     # NA7
    def test63_alpha_deposit(self):
        self.driver.refresh()
        self.navigate_to_new_account()
        self.driver.find_element(By.NAME, "inideposit").send_keys("1234Ace")

        sleep(1)
        message = self.driver.find_element(By.ID, "message19").text
        self.assertEqual(message, "Characters are not allowed")

    # NA8
    def test64_special_char_deposit(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_account()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123@#")

        sleep(1)
        message = self.driver.find_element(By.ID, "message19").text
        self.assertEqual(message, "Special characters are not allowed")

    # NA9
    def test65_space_in_deposit(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_account()
        self.driver.find_element(By.NAME, "inideposit").send_keys("123 12")

        sleep(1)
        message = self.driver.find_element(By.ID, "message19").text
        self.assertEqual(message, "Characters are not allowed")

    # NA10
    def test66_leading_space_in_deposit(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_account()
        self.driver.find_element(By.NAME, "inideposit").send_keys("  ")

        sleep(1)
        message = self.driver.find_element(By.ID, "message19").text
        self.assertEqual(message, "First character cannot have space")

    # NA11
    def test67_valid_savings_account(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_account()
        savings = Select(self.driver.find_element(By.NAME, "selaccount"))
        savings.select_by_visible_text("Savings")

        selected_option = savings.first_selected_option
        assert selected_option.text == "Savings", f"Expected 'Savings', but got {selected_option.text}"

        sleep(2)

    # NA12
    def test68_valid_current_account(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_account()
        savings = Select(self.driver.find_element(By.NAME, "selaccount"))
        savings.select_by_visible_text("Current")

        selected_option = savings.first_selected_option
        assert selected_option.text == "Current", f"Expected 'Savings', but got {selected_option.text}"

    # NA13
    def test69_reset_button(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_account()
        field = self.driver.find_element(By.NAME, "cusid")
        field.send_keys("68805")
        self.driver.find_element(By.NAME, "reset").click()
        sleep(1)
        self.assertEqual(field.get_attribute("value"), "")

    # NA14
    def test70_invalid_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_account()

        self.driver.find_element(By.NAME, "cusid").send_keys("123456")
        self.driver.find_element(By.NAME, "inideposit").send_keys("5000")
        savings = Select(self.driver.find_element(By.NAME, "selaccount"))
        savings.select_by_visible_text("Savings")

        self.driver.find_element(By.NAME, "button2").click()
        sleep(2)
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Customer does not exist!!")
        alert.accept()


    # NA15
    def test71_valid_customer_id(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.navigate_to_new_account()
        self.driver.find_element(By.NAME, "cusid").send_keys("75857")
        self.driver.find_element(By.NAME, "inideposit").send_keys("5000")
        savings = Select(self.driver.find_element(By.NAME, "selaccount"))
        savings.select_by_visible_text("Current")

        self.driver.find_element(By.NAME, "button2").click()
        sleep(2)
        self.assertIn("Account Generated Successfully", self.driver.page_source)

    # NA16
    def test72_continue_button_navigation(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        try:
            self.driver.find_element(By.LINK_TEXT, "Continue").click()
            sleep(2)
            self.assertIn("Manager", self.driver.page_source)
        except Exception as e:
            self.fail(f"Continue link not found or error occurred: {e}")

    # EA1
    def test73_account_number_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()

        self.driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        message = self.driver.find_element(By.ID, "message2")
        self.assertEqual("Account Number must not be blank", message.text)

    # EA2
    def test74_account_number_not_numeric(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()

        self.driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        message = self.driver.find_element(By.ID, "message2")
        self.assertEqual("Characters are not allowed", message.text)

    # EA3
    def test75_account_number_special_char(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()

        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        message = self.driver.find_element(By.ID, "message2")
        self.assertEqual("Special characters are not allowed", message.text)

    # EA4
    def test76_account_number_with_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()

        self.driver.find_element(By.NAME, "accountno").send_keys("123 12")
        message = self.driver.find_element(By.ID, "message2")
        self.assertEqual("Characters are not allowed", message.text)

    # EA5
    def test77_first_character_space(self):

        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()

        self.driver.find_element(By.NAME, "accountno").send_keys("  ")
        message = self.driver.find_element(By.ID, "message2")

        self.assertEqual("First character can not have space", message.text)

    # EA6
    def test78_valid_account_submit(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()

        self.driver.find_element(By.NAME, "accountno").send_keys("143687")
        self.driver.find_element(By.NAME,"AccSubmit").click()
        sleep(2)

        self.assertEqual("Edit Account", self.driver.title)

    # EA7
    def test79_invalid_account_submit(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()

        self.driver.find_element(By.NAME, "accountno").send_keys("00000")
        self.driver.find_element(By.NAME,"AccSubmit").click()
        sleep(1)


        alert = self.driver.switch_to.alert
        self.assertEqual("Account does not exist", alert.text)
        alert.accept()


    # EA8
    def test80_reset_button(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Edit Account").click()
        field = self.driver.find_element(By.NAME, "accountno")
        field.send_keys("123456")
        self.driver.find_element(By.NAME, "res").click()
        sleep(1)
        self.assertEqual(field.get_attribute("value"), "")

        # DA1 - Account number cannot be empty

    def test81_empty_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()

        field = self.driver.find_element(By.NAME, "accountno")
        field.send_keys(Keys.TAB)
        sleep(1)
        error = self.driver.find_element(By.ID, "message2").text
        self.assertEqual(error, "Account Number must not be blank")

        # DA2 - Account number must be numeric

    def test82_account_number_must_be_numeric(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()

        sleep(1)
        field = self.driver.find_element(By.NAME, "accountno")
        field.clear()
        field.send_keys("Acc123")
        sleep(1)
        error = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        self.assertEqual(error, "Characters are not allowed")

        # DA3 - Special characters not allowed

    def test83_account_number_special_characters(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()

        sleep(1)
        field = self.driver.find_element(By.NAME, "accountno")
        field.clear()
        field.send_keys("123!@#")
        sleep(1)
        error = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        self.assertEqual(error, "Special characters are not allowed")

        # DA4 - No blank space in account number

    def test84_account_number_blank_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()

        sleep(1)
        field = self.driver.find_element(By.NAME, "accountno")
        field.clear()
        field.send_keys("123 12")
        sleep(1)
        error = self.driver.find_element(By.XPATH, '//*[@id="message2"]').text
        self.assertEqual(error, "Characters are not allowed")

        # DA5 - First character cannot be space

    def test85_account_number_first_character_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()

        field = self.driver.find_element(By.NAME, "accountno")
        field.clear()
        field.send_keys(" ")
        sleep(1)
        error = self.driver.find_element(By.ID, "message2").text
        self.assertEqual(error, "First character cannot have space")

        # DA6 - Valid account number submit

    def test86_valid_account_number_submit(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()

        field = self.driver.find_element(By.NAME, "accountno")
        field.clear()
        field.send_keys("143710")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()
        sleep(2)
        alert = self.driver.switch_to.alert
        self.assertEqual("Account deleted successfully", alert.text)
        alert.accept()
        alert.accept()


        # DA7 - Invalid account number submit

    def test87_invalid_account_number_submit(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()

        field = self.driver.find_element(By.NAME, "accountno")
        field.clear()
        field.send_keys("12345")
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()
        sleep(2)
        alert = self.driver.switch_to.alert
        self.assertEqual("Account does not exist", alert.text)
        alert.accept()
        alert.accept()



        # DA8 - Reset button test

    def test88_reset_button(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        self.driver.find_element(By.LINK_TEXT, "Delete Account").click()

        field = self.driver.find_element(By.NAME, "accountno")
        field.clear()
        field.send_keys("1234")
        reset_button = self.driver.find_element(By.NAME, "res")
        reset_button.click()
        sleep(1)
        value = self.driver.find_element(By.NAME, "accountno").get_attribute("value")
        self.assertEqual(value, "")

    # BE1: Verify account number cannot be empty
    def test89_blank_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        sleep(1)

        self.driver.find_element(By.NAME, "accountno").send_keys("")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        message = self.driver.find_element(By.ID, "message2").text
        self.assertEqual(message, "Account Number must not be blank")

    # BE2: Account number must be numeric
    def test90_non_numeric_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        sleep(1)

        self.driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        sleep(1)
        message = self.driver.find_element(By.ID, "message2").text
        self.assertEqual(message, "Characters are not allowed")

    # BE3: Account number cannot have special characters
    def test91_special_character_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        sleep(1)

        self.driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        sleep(1)
        message = self.driver.find_element(By.ID, "message2").text
        self.assertEqual(message, "Special characters are not allowed")

    # BE4: First character cannot be space
    def test92_first_character_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        sleep(1)

        self.driver.find_element(By.NAME, "accountno").send_keys(" ")
        sleep(1)
        message = self.driver.find_element(By.ID, "message2").text
        self.assertEqual(message, "First Character can not have space")

    # BE5: Verify Submit Button with a valid account number
    def test93_valid_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        sleep(1)

        self.driver.find_element(By.NAME, "accountno").send_keys("143687")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(3)

        self.assertEqual("Table", self.driver.page_source)

    # BE6: Verify Submit Button with a invalid account number
    def test94_invalid_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        sleep(1)

        self.driver.find_element(By.NAME, "accountno").send_keys("12345")
        self.driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text, "Account does not exist")
        alert.accept()


    # BE7: Verify Reset Button functionality
    def test95_reset_button(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Balance Enquiry").click()
        sleep(1)

        account_field = self.driver.find_element(By.NAME, "accountno")
        account_field.send_keys("123456")
        sleep(1)
        self.driver.find_element(By.NAME, "res").click()
        sleep(1)
        self.assertEqual(account_field.get_attribute("value"), "")

    # MS1: Account number cannot be empty
    def test96_blank_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        sleep(1)
        driver.find_element(By.NAME, "accountno").send_keys("")
        sleep(1)
        driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        message = driver.find_element(By.ID, "message2")
        self.assertEqual(message.text, "Account Number must not be blank")

    # MS2: Account number must be numeric
    def test97_character_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        sleep(1)
        driver.find_element(By.NAME, "accountno").send_keys("Acc123")
        sleep(1)
        message = driver.find_element(By.ID, "message2")
        self.assertEqual(message.text, "Characters are not allowed")

    # MS3: Account number cannot have special characters
    def test98_special_character_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        sleep(1)
        driver.find_element(By.NAME, "accountno").send_keys("!@#")
        sleep(1)
        message = driver.find_element(By.ID, "message2")
        self.assertEqual(message.text, "Special characters are not allowed")

    # MS4: Account number cannot have blank space
    def test99_space_in_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        sleep(1)
        driver.find_element(By.NAME, "accountno").send_keys("123 12")
        sleep(1)
        message = driver.find_element(By.ID, "message2")
        self.assertEqual(message.text, "Characters are not allowed")

    # MS5: First character cannot be a space
    def test100_first_character_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        sleep(1)
        driver.find_element(By.NAME, "accountno").send_keys(" ")
        sleep(1)
        message = driver.find_element(By.ID, "message2")
        self.assertEqual(message.text, "First Character can not have space")

    # MS6: Valid account number
    def test101_valid_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        sleep(1)
        driver.find_element(By.NAME, "accountno").send_keys("143687")
        sleep(1)
        driver.find_element(By.NAME, "AccSubmit").click()
        sleep(3)

        self.assertEqual("Table", self.driver.page_source)

    # MS7: Invalid account number
    def test102_invalid_account_number(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        sleep(1)
        driver.find_element(By.NAME, "accountno").send_keys("12345")
        sleep(1)
        driver.find_element(By.NAME, "AccSubmit").click()
        sleep(1)
        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Account does not exist")
        alert.accept()


    # MS8: Reset button functionality
    def test103_reset_button(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.LINK_TEXT, "Mini Statement").click()
        sleep(1)
        account_number = driver.find_element(By.NAME, "accountno")
        account_number.send_keys("123456")
        sleep(1)
        driver.find_element(By.NAME, "res").click()
        sleep(1)
        self.assertEqual(account_number.get_attribute("value"), "")

    # CS1 : Account number cannot be empty
    def test104_account_number_cannot_be_empty(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "accountno").send_keys("")
        sleep(1)
        driver.find_element(By.NAME, "fdate").click()
        sleep(1)
        message = driver.find_element(By.ID, "message2")
        self.assertEqual(message.text, "Account Number must not be blank")

    # CS2: Account number must be numeric
    def test105_account_number_must_be_numeric(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "accountno").send_keys("1234")
        sleep(1)

        message = driver.find_element(By.ID, "message2")
        self.assertEqual(message.text, "Characters are not allowed")

    # CS3: Account number cannot have special character
    def test106_account_number_cannot_have_special_character(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "accountno").send_keys("123!@#")
        sleep(1)

        message = driver.find_element(By.ID, "message2")
        self.assertEqual(message.text, "Special characters are not allowed")

    # CS4: Account number cannot have blank space
    def test107_account_number_cannot_have_blank_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "accountno").send_keys("123 12")
        sleep(1)

        message = driver.find_element(By.ID, "message2")
        self.assertEqual(message.text, "Characters are not allowed")

    # CS5: First Character cannot be space
    def test108_first_character_cannot_be_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "accountno").send_keys(" ")
        sleep(1)

        message = driver.find_element(By.ID, "message2")
        self.assertEqual(message.text, "First Character can not have space")

    # CS6 : click on the date field
    def test109_from_date_field_must_not_be_blank(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "fdate").click()
        sleep(1)

        message = driver.find_element(By.ID, "message26")
        self.assertEqual(message.text, "From Date Field must not be blank")

    # CS7: click on the date field
    def test110_to_date_field_must_not_be_blank(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)
        driver.find_element(By.NAME, "tdate").click()
        sleep(1)

        # confirming the message that will pop out
        message = driver.find_element(By.ID, "message27")
        self.assertEqual(message.text, "From Date Field must not be blank")

    # CS8 : Minimum Transaction Value must be numeric
    def test111_minimum_transaction_value_must_be_numeric(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "amountlowerlimit").send_keys("1234")
        sleep(1)

        message = driver.find_element(By.ID, "message12")
        self.assertEqual(message.text, "Characters are not allowed")

    # CS9 : Minimum Transaction Value cannot have special character
    def test112_minimum_transaction_value_cannot_have_special_character(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "amountlowerlimit").send_keys("123!@#")
        sleep(1)

        message = driver.find_element(By.ID, "message12")
        self.assertEqual(message.text, "Special characters are not allowed")

    # CS10 : Minimum Transaction Value cannot have blank space
    def test113_minimum_transaction_value_cannot_have_blank_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "amountlowerlimit").send_keys("123 12")
        sleep(1)

        message = driver.find_element(By.ID, "message12")
        self.assertEqual(message.text, "Characters are not allowed")

    # CS11 : First Character cannot be space
    def test114_first_character_of_minimum_transaction_cannot_be_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "amountlowerlimit").send_keys(" ")
        sleep(1)

        message = driver.find_element(By.ID, "message12")
        self.assertEqual(message.text, "First Character can not have space")

    # CS12: Number of transaction must be numeric
    def test115_number_of_transaction_must_be_numeric(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "numtransaction").send_keys("Acc123")
        sleep(1)

        message = driver.find_element(By.ID, "message13")
        self.assertEqual(message.text, "Characters are not allowed")

    # CS13: Number of transaction have special character
    def test116_number_of_transaction_cannot_have_special_character(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)
        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "numtransaction").send_keys("123!@#")
        sleep(2)

        message = driver.find_element(By.ID, "message13")
        self.assertEqual(message.text, "Number of Transaction cannot have special character")

    # CS14: Number of transaction cannot have blank space
    def test117_number_of_transaction_cannot_have_blank_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "numtransaction").send_keys("123 12")
        sleep(2)

        message = driver.find_element(By.ID, "message13")
        self.assertEqual(message.text, "Characters are not allowed")

    # CS15: First Character cannot be space
    def test118_first_character_of_number_of_transaction_cannot_be_space(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "numtransaction").send_keys(" ")
        sleep(2)

        message = driver.find_element(By.ID, "message13")
        self.assertEqual(message.text, "First Character can not have space")

    # CS16 : Reset Button functionality
    def test119_reset_button(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "accountno").send_keys("123456")
        sleep(1)
        driver.find_element(By.NAME, "fdate").send_keys("0020250401")
        sleep(1)
        driver.find_element(By.NAME, "tdate").send_keys("0020250403")
        sleep(1)
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("20")
        sleep(1)
        driver.find_element(By.NAME, "numtransaction").send_keys("3")
        sleep(1)
        driver.find_element(By.NAME, "res").click()
        sleep(2)

        # Verify that all fields are reset
        self.assertEqual(driver.find_element(By.NAME, "accountno").get_attribute('value'), "")
        self.assertEqual(driver.find_element(By.NAME, "fdate").get_attribute('value'), "")
        self.assertEqual(driver.find_element(By.NAME, "tdate").get_attribute('value'), "")
        self.assertEqual(driver.find_element(By.NAME, "amountlowerlimit").get_attribute('value'), "")
        self.assertEqual(driver.find_element(By.NAME, "numtransaction").get_attribute('value'), "")

    # CS17 : Valid Account Number, Valid From Date, Blank To Date, valid Minimum Transaction Value and valid Number of Transaction
    def test120_verify_submit_button(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/V4/manager/Managerhomepage.php")
        sleep(3)

        driver.find_element(By.XPATH, "/html/body/div[3]/div/ul/li[14]/a").click()
        sleep(1)

        driver.find_element(By.NAME, "accountno").send_keys("143687")
        sleep(1)
        driver.find_element(By.NAME, "fdate").send_keys("0020250401")
        sleep(1)
        driver.find_element(By.NAME, "tdate").send_keys("")
        sleep(1)
        driver.find_element(By.NAME, "amountlowerlimit").send_keys("20")
        sleep(1)
        driver.find_element(By.NAME, "numtransaction").send_keys("3")
        sleep(1)
        driver.find_element(By.NAME, "AccSubmit").click()
        sleep(2)

        alert = driver.switch_to.alert
        self.assertEqual(alert.text, "Please fill all fields")
        alert.accept()











