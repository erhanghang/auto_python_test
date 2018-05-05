#-*- coding:utf-8 -*-
#author:yupeng
from selenium import webdriver
import time
import unittest
from page.loginPage import login,liulanqi

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
        self.driver=liulanqi()


    def tearDown(self):
        '''关闭浏览器，退出浏览器进程'''
        self.driver.quit()

    def test_axxlogin_01(self):
        '''测试正常登录'''
        title=login(self.driver,'13021258755','qaz123')
        self.assertIn("教研",title)

    def test_axxlogin_02(self):
        '''测试异常登录'''
        title=login(self.driver,'13021258755','qaz456')
        self.assertIn("教研",title)

if __name__=='__main__':
    unittest.main()
