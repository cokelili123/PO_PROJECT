from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class Display(BaseAction):
    # 显示按钮
    display_button = By.XPATH,"//*[contains(@text,'显示')]"
    # 搜索按钮
    search_button=By.ID,"com.android.settings:id/search"
    #　搜索输入框
    search_input = By.XPATH,"//*[contains(@text,'搜索…')]"
    # 返回按钮
    back_button = By.CLASS_NAME,"android.widget.ImageButton"
    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        self.driver = driver
    def click_display(self):

        # self.driver.find_element_by_xpath("//*[contains(@text,'显示')]").click()
        self.find_element(self.display_button).click()

    def click_search(self):
        # self.driver.find_element_by_id("com.android.settings:id/search").click()
        self.find_element(self.search_button).click()

    def input_text(self,text):
        # self.driver.find_element_by_xpath("//*[contains(@text,'搜索…')]").send_keys(text)
        self.find_element(self.search_input).send_keys(text)

    def click_back(self):

        # self.driver.find_element_by_class_name("android.widget.ImageButton").click()
        self.find_element(self.back_button).click()
    def find_element(self,loc):
        return self.driver.find_element(loc[0],loc[1])
