from selenium.webdriver.common.by import By


class NetworkPage:
    # 更多按钮
    more_button = By.XPATH,"//*[contains(@text,'更多')]"
    # 移动网络按钮
    mobile_button = By.XPATH,"//*[contains(@text,'移动网络')]"
    # 首选网络按钮
    first_network = By.XPATH,"//*[contains(@text,'首选网络类型')]"
    # 3G按钮
    button_3G = By.XPATH,"//*[contains(@text,'3G')]"
    # 2Ga按钮
    button_2G = By.XPATH,"//*[contains(@text,'2G')]"
    def __init__(self,driver):
        self.driver = driver

    def click_more(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'更多')]").click()
        self.find_element(self.more_button).click()

    def click_move_network(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'移动网络')]").click()
        self.find_element(self.mobile_button).click()

    def click_network_first(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'首选网络类型')]").click()
        self.find_element(self.first_network).click()

    def click_3G(self):

        # self.driver.find_element_by_xpath("//*[contains(@text,'3G')]").click()
        self.find_element(self.button_3G).click()

    def click_2G(self):
        # self.driver.find_element_by_xpath("//*[contains(@text,'2G')]").click()
        self.find_element(self.button_2G).click()

    def find_element(self,loc):
        return self.driver.find_element(loc[0],loc[1])