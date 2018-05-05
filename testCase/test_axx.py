#-*- coding:utf-8 -*-
#author:yupeng
from selenium import webdriver
import time
import unittest

class axx_test(unittest.TestCase):
    ''' 爱学习登录测试'''
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        '''打开系统做统一处理'''
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("http://www.aixuexi.com")
        self.driver.implicitly_wait(20)

    def tearDown(self):
        '''关闭浏览器，退出浏览器进程'''
        self.driver.quit()

    def test_axxlogin_01(self):
        '''测试正常登录'''
        driver=self.driver
        driver.find_element_by_css_selector("#username").send_keys("13021258755")
        time.sleep(1)
        driver.find_element_by_css_selector("#password").send_keys("qaz123")
        time.sleep(1)
        driver.find_element_by_css_selector("#submit").click()
        time.sleep(3)
        title=driver.title
        self.assertIn("教研",title)

    def test_axxlogin_02(self):
        '''测试异常登录'''
        self.driver.find_element_by_css_selector("#username").send_keys("13021258755")
        time.sleep(1)
        self.driver.find_element_by_css_selector("#password").send_keys("qaz456")
        time.sleep(1)
        self.driver.find_element_by_css_selector("#submit").click()
        time.sleep(3)
        self.assertIn("教研",self.driver.title)

if __name__=='__main__':
    unittest.main()
