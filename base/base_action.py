from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:
    def __init__(self,driver):
        self.driver = driver
    def click(self,loc):
        self.find_element(loc).click()
    def find_element(self,loc):
       return WebDriverWait(self.driver,5,1).until(lambda x:x.find_element(loc[0],loc[1]))

