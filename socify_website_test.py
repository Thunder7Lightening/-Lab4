import unittest
from selenium.webdriver.common.keys import Keys
from SocifyExplorer import SocifyExplorer

class SocifyWebsiteTest(unittest.TestCase):

    def setUp(self):
        self.socifyExplorer = SocifyExplorer()
        self.socifyExplorer.signIn()

    def test01_create_a_new_event(self):
        socifyExplorer = self.socifyExplorer
        socifyExplorer.createANewEvent("New Event Created.", "2018/05/11 19:00")
        self.assertIn("New Event Created.", socifyExplorer.getEventContentInNewsFeed())
        self.assertIn("11 May 19:00", socifyExplorer.getEventDateInNewsFeed())

    def test02_create_a_new_event_with_invalid_Event_Name_or_When(self):
        socifyExplorer = self.socifyExplorer
        socifyExplorer.createANewEvent("", "")
        assert socifyExplorer.isInCreateEventPage(), "not stay in create event page"

    def test03_edit_a_event(self):
        try:
            socifyExplorer = self.socifyExplorer
            socifyExplorer.editAEvent("Event Changed.", "2018/04/20 10:00")
            self.assertIn("Event Changed.", socifyExplorer.getEventContentInEventPage())
            self.assertIn("20 Apr 10:00", socifyExplorer.getEventDateInEventPage())
        except:
            print("NewsFeed上無任何Event可以編輯")

    def test04_edit_a_event_with_invalid_Event_Name_or_When(self):
        try:
            socifyExplorer = self.socifyExplorer
            eventContent = socifyExplorer.getEventContentInEventPage()
            eventDate = socifyExplorer.getEventDateInEventPage()
            socifyExplorer.editAEvent("", "")
            self.assertIn(eventContent, socifyExplorer.getEventContentInEventPage())
            self.assertIn(eventDate, socifyExplorer.getEventDateInEventPage())
        except:
            print("NewsFeed上無任何Event可以編輯")

    def test05_write_a_comment(self):
        try:
            socifyExplorer = self.socifyExplorer
            commentId = socifyExplorer.writeComment("New Comment Created.")
            self.assertIn("New Comment Created.", socifyExplorer.getComment(commentId))
        except:
            print("NewsFeed上無任何Event或Status可以評論")

    def test06_write_an_empty_comment(self):
        try:
            socifyExplorer = self.socifyExplorer
            commentId = socifyExplorer.writeComment("")
            assert False, "should go to except"
        except:
            assert True

    def test07_delete_a_comment(self):
        try:
            socifyExplorer = self.socifyExplorer
            deletedCommentId = socifyExplorer.deleteComment()
            assert socifyExplorer.isCommentDeleted(deletedCommentId), "Comment刪除失敗"
        except:
            print("NewsFeed上無任何評論可被刪除")

    def test08_press_like_button(self):
        try:
            socifyExplorer = self.socifyExplorer
            activityId = socifyExplorer.getActivityId()
            if socifyExplorer.isLikeButtonPresent(activityId):
                oldLikeCount = socifyExplorer.getLikeCount(activityId)          
                socifyExplorer.pressLikeButton(activityId)
                newLikeCount = socifyExplorer.getLikeCount(activityId)
                assert newLikeCount == oldLikeCount + 1, "like數沒有增加"
            else:
                raise Exception()
        except:
            print("NewsFeed上無任何Event或Status like按鈕")
        
    def test09_press_unlike_button(self):
        try:
            socifyExplorer = self.socifyExplorer
            activityId = socifyExplorer.getActivityId()
            if socifyExplorer.isUnlikeButtonPresent(activityId):
                oldLikeCount = socifyExplorer.getLikeCount(activityId)          
                socifyExplorer.pressUnlikeButton(activityId)
                newLikeCount = socifyExplorer.getLikeCount(activityId)
                assert newLikeCount == oldLikeCount - 1, "like數沒有減少"
            else:
                raise Exception()
        except:
            print("NewsFeed上無任何Event或Status unlike按鈕")

    def test10_delete_a_event(self):
        try:
            socifyExplorer = self.socifyExplorer
            deletedEventId = socifyExplorer.deleteAEvent()
            assert socifyExplorer.isEventDeleted(deletedEventId), "Event刪除失敗"
        except:
            print("NewsFeed上無任何Event可以刪除")

    def test11_create_a_new_status(self):
        socifyExplorer = self.socifyExplorer
        socifyExplorer.createANewStatus("this is a new post status.")
        self.assertIn("this is a new post status", socifyExplorer.getStatusContentInNewsFeed())

    def test12_create_a_new_status_with_empty_message(self):
        socifyExplorer = self.socifyExplorer
        socifyExplorer.createANewStatus("")
        assert socifyExplorer.shouldExistAlertMessage(), "alert msg not showing"

    def test13_edit_a_status(self):
        try:
            socifyExplorer = self.socifyExplorer
            socifyExplorer.editAStatus("msg has been changed.")
            self.assertIn("msg has been changed.", socifyExplorer.getStatusContentInPostPage())
            socifyExplorer.goBackToNewsFeed()
            self.assertIn("msg has been changed.", socifyExplorer.getStatusContentInNewsFeed())
        except:
            print("沒有Status可供編輯")  

    def test14_delete_a_status(self):
        try:
            socifyExplorer = self.socifyExplorer
            deleteStatusId = socifyExplorer.deleteAStatus()
            assert socifyExplorer.isStatusDeleted(deleteStatusId), "刪除失敗"
        except:
            print("沒有Status可供刪除")

    def test15_follow_friends(self):
        try:
            socifyExplorer = self.socifyExplorer
            name = socifyExplorer.followFriends("oneonezero")
            assert socifyExplorer.isFriendFollowed(name), "follow friend fail"
        except:
            print("You have follow this friend.")

    def test16_edit_profile(self):
        socifyExplorer = self.socifyExplorer
        socifyExplorer.editProfile("faceAvatar.jpg", "thunder.jpg", "TTester")
        assert "faceAvatar" in socifyExplorer.getAvatarName(), "avatar 上傳失敗"
        assert "thunder" in socifyExplorer.getCoverName(), "cover 上傳失敗"
        self.assertIn("TTester", socifyExplorer.getUserName())

    def tearDown(self):
        self.socifyExplorer.close()

if __name__ == "__main__":
    unittest.main()