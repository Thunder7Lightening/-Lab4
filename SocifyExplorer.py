from selenium import webdriver
from SocifyStatusManager import SocifyStatusManager
from SocifyLoginExecuter import SocifyLoginExecuter
from SocifyEventManager import SocifyEventManager
from SocifyCommentManager import SocifyCommentManager
from SocifyActivityManager import SocifyActivityManager
from SocifyProfileManager import SocifyProfileManager
from SocifyFriendManager import SocifyFriendManager

class SocifyExplorer:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.loginExecuter = SocifyLoginExecuter(self.driver)
        self.statusManager = SocifyStatusManager(self.driver)
        self.socifyEventManager = SocifyEventManager(self.driver)
        self.socifyCommentManager = SocifyCommentManager(self.driver)
        self.socifyActivityManager = SocifyActivityManager(self.driver)
        self.socifyProfileManager = SocifyProfileManager(self.driver)
        self.socifyFriendManager = SocifyFriendManager(self.driver)

    def isInPostPage(self):
        return "posts" in self.driver.current_url

    def isInCreateEventPage(self):
        return "events" in self.driver.current_url

    def isEventDeleted(self, deletedEventId):
        return self.socifyEventManager.isEventDeleted(deletedEventId)

    def isStatusDeleted(self, deletedStatusId):
        return self.statusManager.isStatusDeleted(deletedStatusId)

    def isCommentDeleted(self, deletedCommentId):
        return self.socifyCommentManager.isCommentDeleted(deletedCommentId)

    def isLikeButtonPresent(self, activityId):
        return self.socifyActivityManager.isLikeButtonPresent(activityId)

    def isUnlikeButtonPresent(self, activityId):
        return self.socifyActivityManager.isUnlikeButtonPresent(activityId)

    def shouldExistAlertMessage(self):
        return self.statusManager.shouldExistAlertMessage()

    def signIn(self):
        self.loginExecuter.login()

    def createANewEvent(self, msg, date):
       self.socifyEventManager.createANewEvent(msg, date)

    def editAEvent(self, msg, date):
        self.socifyEventManager.editAEvent(msg, date)

    def deleteAEvent(self):
        return self.socifyEventManager.deleteAEvent()

    def writeComment(self, msg):
        return self.socifyCommentManager.writeComment(msg)

    def deleteComment(self):
        return self.socifyCommentManager.deleteComment()

    def getComment(self, commentId):
        return self.socifyCommentManager.getComment(commentId)

    def getActivityId(self):
        return self.socifyActivityManager.getActivityId()

    def getLikeCount(self, activityId):
        return self.socifyActivityManager.getLikeCount(activityId)

    def pressLikeButton(self, activityId):
        self.socifyActivityManager.pressLikeButton(activityId)

    def pressUnlikeButton(self, activityId):
        self.socifyActivityManager.pressUnlikeButton(activityId)

    def getEventContentInNewsFeed(self):
        return self.socifyEventManager.getEventContentInNewsFeed()

    def getEventDateInNewsFeed(self):
        return self.socifyEventManager.getEventDateInNewsFeed()

    def getEventContentInEventPage(self):
        return self.socifyEventManager.getEventContentInEventPage()

    def getEventDateInEventPage(self):
        return self.socifyEventManager.getEventDateInEventPage()

    def followFriends(self, name):
        return self.socifyFriendManager.followFriends(name)

    def isFriendFollowed(self, name):
        return self.socifyFriendManager.isFriendFollowed(name)
        
    def editProfile(self, avatar, cover, name):
        self.socifyProfileManager.editProfile(avatar, cover, name)

    def getAvatarName(self):
        return self.socifyProfileManager.getAvatarName()

    def getUserName(self):
        return self.socifyProfileManager.getUserName()
        
    def getCoverName(self):
        return self.socifyProfileManager.getCoverName()

    def getStatusContentInNewsFeed(self):
        return self.statusManager.getStatusContentInNewsFeed()

    def getStatusContentInPostPage(self):
        return self.statusManager.getStatusContentInPostPage()

    def createANewStatus(self, msg):
        self.statusManager.createANewStatus(msg)

    def editAStatus(self, msg):
        self.statusManager.editAStatus(msg)

    def deleteAStatus(self):
        return self.statusManager.deleteAStatus()

    def goBackToNewsFeed(self):
        self.driver.find_element_by_link_text("Socify").click()

    def close(self):
        self.driver.close()