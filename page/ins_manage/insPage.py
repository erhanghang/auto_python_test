#-*- coding:utf-8 -*-
#author:yupeng
#机构页面
from common.base import basePage
import time
ins_name='YP测试机构-于鹏专用'

class insPage(basePage):
    '''查询机构'''
    insmanage_loc=('xpath','//ul/li[2]/a')
    ins_loc=('xpath','//a[text()=\'机构（新）\']')
    insname_loc=('xpath','//form/div[1]/div[1]/div/div[2]/div/div/input')
    instype_loc=('xpath','//form/div[2]/div[1]/div/div[2]/div/div/div/div/div')
    testins_loc=('xpath','//li[text()=\'测试机构\']')
    querybutton_loc=('xpath','//form/div[6]/div/button[1]')
    assertinsname_loc=('xpath','//table/tbody/tr/td[3]/a')

    def click_insmanage(self):
        '''点击机构管理'''
        self.click_element(self.insmanage_loc)

    def click_ins(self):
        '''点击机构新'''
        self.click_element(self.ins_loc)

    def input_insname(self):
        '''输入机构名称'''
        self.sendkeys(self.insname_loc,ins_name)

    def select_instype(self):
        '''选择测试机构'''
        self.click_element(self.instype_loc)
        time.sleep(1)
        self.click_element(self.testins_loc)

    def click_querybutton(self):
        '''点击查询按钮'''
        self.click_element(self.querybutton_loc)

    def assertinsname(self):
        result=self.is_text_in_element(self.assertinsname_loc,ins_name)
        assert result==True,'查询机构不正确'