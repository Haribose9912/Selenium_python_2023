from selenium.webdriver.common.by import By


class Loginpage:
    signin_button = "//input[@id='signInSubmitButton']"
    textbox_mobilenumber = "//div//input[@id='mobilemy']"
    submit_button = "//button[text()='Submit']"
    loginWithPassword_bt = "//input[@value='Login with Password']"
    textbox_password = "//input[@type='password']"
    view_profile_bt = "//a[text()='View Profile']"
    User_Greetings = "//a[text()='Hi ']"
    signout_button = "//a[text()='Sign Out']"

    def __init__(self, driver):
        # super().__init__(driver)
        self.driver = driver

    def setmobilenumber(self, mobilenumber):
        self.driver.find_element(By.XPATH, self.textbox_mobilenumber).clear()
        self.driver.find_element(By.XPATH, self.textbox_mobilenumber).send_keys(mobilenumber)

    def setpassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password).clear()
        self.driver.find_element(By.XPATH, self.textbox_password).send_keys(password)

    def clicksignin(self):
        self.driver.find_element(By.XPATH, self.signin_button).click()

    def clicksignout(self):
        self.driver.find_element(By.XPATH, self.signout_button).click()

    def submitbtn(self):
        self.driver.find_element(By.XPATH, self.submit_button).click()

    def viewprofilebtn(self):
        self.driver.find_element(By.XPATH, self.view_profile_bt).click()

    def userGreetingsbtn(self):
        self.driver.find_element(By.XPATH, self.User_Greetings).click()

    def loginwithpasswordbtn(self):
        self.driver.find_element(By.XPATH, self.loginWithPassword_bt).click()
