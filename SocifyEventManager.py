class SocifyEventManager:
    def __init__(self, driver):
        self.driver = driver

    def isEventDeleted(self, deletedEventId):
        try:
            self.driver.find_element_by_id(deletedEventId)
            return False
        except:
            return True

    def createANewEvent(self, msg, date):
        self.driver.find_element_by_link_text("Create Event").click()
        self.driver.find_element_by_css_selector("input#event_name.form-control").send_keys(msg)
        self.driver.find_element_by_css_selector("input#event_event_datetime.form-control").send_keys(date)
        self.driver.find_element_by_css_selector("input.btn.btn-primary").click()

    def editAEvent(self, msg, date):
        # press edit button
        activityEvent = self.driver.find_element_by_css_selector("div.activity-event")
        editButton = activityEvent.find_element_by_css_selector("a.btn-primary")
        editButton.click()
        # edit Event name and When
        eventNameTextbox = self.driver.find_element_by_css_selector("input#event_name.form-control")
        eventNameTextbox.clear()
        eventNameTextbox.send_keys(msg)
        whenTextbox = self.driver.find_element_by_css_selector("input#event_event_datetime.form-control")
        whenTextbox.clear()
        whenTextbox.send_keys(date)
        # press update
        self.driver.find_element_by_css_selector("input.btn.btn-primary").click()

    def deleteAEvent(self):
        # locate event & get eventId
        activityEvent = self.driver.find_element_by_css_selector("div.activity-event")
        eventId = activityEvent.get_attribute("id")
        # press delete button & return eventId
        editButton = activityEvent.find_element_by_css_selector("a.btn-danger")
        editButton.click()
        return eventId

    def getEventContentInNewsFeed(self):
        activityEvent = self.driver.find_element_by_css_selector("div.activity-event")
        return activityEvent.find_element_by_css_selector("h3").text

    def getEventDateInNewsFeed(self):
        activityEvent = self.driver.find_element_by_css_selector("div.activity-event")
        return activityEvent.find_element_by_css_selector("span.text").text

    def getEventContentInEventPage(self):
        return self.driver.find_element_by_css_selector("h3").text

    def getEventDateInEventPage(self):
        return self.driver.find_element_by_css_selector("span.text").text
