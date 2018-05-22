class SocifyStatusManager:
    def __init__(self, driver):
        self.driver = driver

    def isStatusDeleted(self, deletedStatusId):
        driver = self.driver
        try:
            driver.find_element_by_id(deletedStatusId)
            return False
        except:
            return True

    def shouldExistAlertMessage(self):
        try:
            self.driver.find_element_by_css_selector("div.alert.alert-info")
            return True
        except:
            return False

    def createANewStatus(self, msg):
        # type something into "What's up?" field and press "Post"
        driver = self.driver
        postContent = driver.find_element_by_id("post-content")
        postContent.clear()
        postContent.send_keys(msg)
        self.driver.find_element_by_name("commit").click()

    def getStatusContentInNewsFeed(self):
        return self.driver.find_element_by_class_name("activity-post").find_element_by_class_name("text").find_element_by_tag_name("p").text

    def getStatusContentInPostPage(self):
        return self.driver.find_element_by_class_name("content").find_element_by_tag_name("p").text

    def editAStatus(self, msg):
        driver = self.driver
        # press edit button
        driver.find_element_by_class_name("activity-post").find_element_by_class_name("btn-primary").click()
        # type new msg
        postContent = driver.find_element_by_id("post-content")
        postContent.clear()
        postContent.send_keys(msg)
        # press post button
        driver.find_element_by_name("commit").click()

    def deleteAStatus(self):
        driver = self.driver
        # locate status
        status = driver.find_element_by_css_selector("div#activities").find_element_by_css_selector("div.activity-post")
        statusId = status.get_attribute("id")
        # press delete
        deleteButton = status.find_element_by_css_selector("a.btn.btn-danger.btn-sm")
        deleteButton.click()
        # return deleted status id
        return statusId