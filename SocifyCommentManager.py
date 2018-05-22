class SocifyCommentManager:
    def __init__(self, driver):
        self.driver = driver

    def isCommentDeleted(self, deletedCommentId):
        try:
            self.driver.find_element_by_id(deletedCommentId)
            return False
        except:
            return True

    def writeComment(self, msg):
        commentButton = self.driver.find_element_by_css_selector("a.btn.btn-block")
        commentButton.click()

        commentTextbox = self.driver.find_element_by_css_selector("div#comment-text.editable")
        commentTextbox.clear()
        commentTextbox.send_keys(msg)

        commentButton = self.driver.find_element_by_css_selector("input.btn.btn-primary")
        commentButton.click()

        commentsTextbox = self.driver.find_element_by_css_selector("div.comments")
        commentId = commentsTextbox.find_element_by_tag_name("div").get_attribute("id")
        return commentId

    def deleteComment(self):
        commentButton = self.driver.find_element_by_css_selector("a.btn.btn-block")
        commentButton.click()

        commentsTextbox = self.driver.find_element_by_css_selector("div.comments")
        firstCommentTextbox = commentsTextbox.find_element_by_tag_name("div")
        commentId = firstCommentTextbox.get_attribute("id")
        deleteButton = firstCommentTextbox.find_element_by_css_selector("a.btn.btn-danger.btn-sm")
        deleteButton.click()
        return commentId

    def getComment(self, commentId):
        commentTextbox = self.driver.find_element_by_id(commentId)
        comment = commentTextbox.find_element_by_css_selector("p").text
        return comment