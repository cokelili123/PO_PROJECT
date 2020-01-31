from time import time

from appium import webdriver
from base.base_driver import init_driver
from page.network_page import NetworkPage


class TestNetwork:
    def setup(self):
        self.driver=init_driver()
        self.network_page = NetworkPage(self.driver)


    def test_network_3g(self):
        # 点击更多
        self.network_page.click_more()
        # 点击移动网络
        self.network_page.click_move_network()
        # 点击首选网络类型
        self.network_page.click_network_first()
        # 点击3G
        self.network_page.click_3G()



    def test_network_2g(self):
        # 点击更多
        self.network_page.click_more()
        # 点击移动网络
        self.network_page.click_move_network()
        # 点击首选类型网络
        self.network_page.click_network_first()
        # 点击2G
        self.network_page.click_2G()

  def test_network_4g(self):
        # 点击更多
        self.network_page.click_more()
        # 点击移动网络
        self.network_page.click_move_network()
        # 点击首选类型网络
        self.network_page.click_network_first()
        # 点击2G
        self.network_page.click_4G()
  def test_network_5g(self):
        # 点击更多
        self.network_page.click_more()
        # 点击移动网络
        self.network_page.click_move_network()
        # 点击首选类型网络
        self.network_page.click_network_first()
        # 点击2G
        self.network_page.click_5G()
  def test_network_9g(self):
        # 点击更多
        self.network_page.click_more()
        # 点击移动网络
        self.network_page.click_move_network()
        # 点击首选类型网络
        self.network_page.click_network_first()
        # 点击2G
        self.network_page.click_6G()
 

# 2

