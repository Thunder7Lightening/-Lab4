class SocifyActivityManager:
    def __init__(self, driver):
        self.driver = driver

    def getActivityId(self):
        try:
            activity = self.driver.find_element_by_css_selector("div.activity-post")
            likeButtonExist = activity.find_element_by_css_selector("button.btn.btn-block")
            return activity.get_attribute("id")
        except:
            pass
        
        activity = self.driver.find_element_by_css_selector("div.activity-event")
        likeButtonExist = activity.find_element_by_css_selector("button.btn.btn-block")
        return activity.get_attribute("id")

    def getLikeCount(self, activityId):
        activity = self.driver.find_element_by_id(activityId)
        likeCountText = activity.find_element_by_css_selector("span.like-count").text
        likeCount = likeCountText.split(' ', 1)[0]
        return int(likeCount)

    def pressLikeButton(self, activityId):
        activity = self.driver.find_element_by_id(activityId)
        likeButton = activity.find_element_by_css_selector("button.btn.btn-block")
        likeButton.click()

    def pressUnlikeButton(self, activityId):
        self.pressLikeButton(activityId)

    def isLikeButtonPresent(self, activityId):
        likeOrUnlikeButton = self.driver.find_element_by_css_selector("button.btn.btn-block")
        return likeOrUnlikeButton.text == "like"

    def isUnlikeButtonPresent(self, activityId):
        return not self.isLikeButtonPresent(activityId)
            
            

        