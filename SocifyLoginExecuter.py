class SocifyLoginExecuter:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get("http://140.124.183.102:3000/")
        # press sign in
        self.driver.find_element_by_link_text("Sign in").click()
        # type email and password, and then log in
        self.driver.find_element_by_id("user_email").send_keys("thunder7lightening@gmail.com")
        self.driver.find_element_by_id("user_password").send_keys("test1234")
        self.driver.find_element_by_name("commit").click()