class SocifyFriendManager:
    def __init__(self, driver):
        self.driver = driver

    def followFriends(self, name):
        driver = self.driver
        driver.get("http://140.124.183.102:3000/users/" + name)

        profile = driver.find_element_by_css_selector("div#user-info.well")
        followButton = profile.find_element_by_css_selector("button.btn.btn-success")
        followButton.click()

        friendName = profile.find_element_by_css_selector("div.text-center").find_element_by_css_selector("h5").find_element_by_tag_name("a").text
        return friendName

    def isFriendFollowed(self, name):
        driver = self.driver
        driver.get("http://140.124.183.102:3000/")
        driver.find_element_by_css_selector("div#links.well").find_element_by_link_text("Friends").click()
        
        try:
            driver.find_element_by_css_selector("div#friends").find_element_by_link_text(name)
            return True
        except:
            return False


