#-*- coding:utf-8 -*-
#author:yupeng

from selenium import webdriver
import unittest
import  time

class Test1(unittest.TestCase):
    u'''百度页测试'''

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # def setUp(self):
    #     self.driver = webdriver.Firefox()
    # def tearDown(self):
    #     self.driver.quit()

    def test_01(self):
        u'''测试通过案例'''
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys(u'百度一下')
        self.driver.find_element_by_id('su').click()
        self.assertTrue(True)

    def test_02(self):
        u'''测试通过案例'''
        self.driver.get("http://www.cnblogs.com/yoyoketang/")
        self.assertIn(u"上海",self.driver.title)

    # def test_03(self):
    #      u'''测试异常登录'''
    # #     #driver=self.driver
    # #     self.driver.maximize_window()
    # #     self.driver.get("http://www.aixuexi.com")
    # #     self.driver.implicitly_wait(20)
    # #     self.driver.find_element_by_css_selector("#username").send_keys("13021258755")
    # #     time.sleep(1)
    # #     self.driver.find_element_by_css_selector("#password").send_keys("qaz456")
    # #     time.sleep(1)
    # #     self.driver.find_element_by_css_selector("#submit").click()
    # #     time.sleep(3)
    # #     self.assertIn("教研",self.driver.title)
    #      self.driver.get("http://www.cnblogs.com/yoyoketang/")
    #      self.assertIn(u"上海4343434",self.driver.title)

if __name__ == "__main__":
    unittest.main()