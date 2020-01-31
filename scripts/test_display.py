import os,sys
sys.path.append(os.getcwd())
from time import time

from appium import webdriver
from base.base_driver import init_driver
from page.display_page import Display


class TestDisplay:
    def setup(self):
        self.driver=init_driver()
        self.display_page = Display(self.driver)



    
    def test_display_search(self):

      # 点击显示
      self.display_page.click_display()
      # 点击放大镜
      self.display_page.click_search()
      # 输入hello
      self.display_page.input_text("hello")
      # 点击返回
      self.display_page.click_back()

     def test_display_search9(self):

      # 点击显示
      self.display_page.click_display()
      # 点击放大镜
      self.display_page.click_search()
      # 输入hello
      self.display_page.input_text("hello")
      # 点击返回
      self.display_page.click_back()



