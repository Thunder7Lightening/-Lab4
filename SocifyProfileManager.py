import os

class SocifyProfileManager:
    def __init__(self, driver):
        self.driver = driver

    def editProfile(self, avatar, cover, name):
        driver = self.driver
        editProfileLink = self.driver.find_element_by_css_selector("div#links.well").find_element_by_link_text("Edit Profile")
        editProfileLink.click()

        avatarInput = driver.find_element_by_css_selector("input#user_avatar")
        avatarInput.clear()
        avatarInput.send_keys(os.path.abspath(os.path.dirname(avatar)) + "\\" + avatar)

        coverInput = driver.find_element_by_css_selector("input#user_cover")
        coverInput.clear()
        coverInput.send_keys(os.path.abspath(os.path.dirname(cover)) + "\\" + cover)

        nameInput = driver.find_element_by_css_selector("input#user_name.form-control")
        nameInput.clear()
        nameInput.send_keys(name)

        updateButton = driver.find_element_by_css_selector("input.btn.btn-primary")
        updateButton.click()

    def getAvatarName(self):
        driver = self.driver
        profile = driver.find_element_by_css_selector("div#user-info.well").find_element_by_css_selector("div.text-center")
        avatarImage = profile.find_element_by_css_selector("img.avatar")
        return avatarImage.get_attribute("src")

    def getCoverName(self):
        driver = self.driver
        cover = driver.find_element_by_css_selector("div.cover")
        return cover.get_attribute("style")

    def getUserName(self):
        driver = self.driver
        profile = driver.find_element_by_css_selector("div#user-info.well").find_element_by_css_selector("div.text-center").find_element_by_tag_name("h5")
        return profile.text