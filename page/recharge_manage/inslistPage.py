#-*- coding:utf-8 -*-
#author:yupeng
from common.base import basePage

class inslistPage(basePage):
    '''客户管理页面'''
    rechargemanage_loc=('xpath','//ul/li[5]/a')
    #inslist_loc=('link_text','客户管理')
    inslist_loc=('xpath','//a[text()="客户管理"]')
    instype_loc=('id','insType')
    insname_loc=('xpath','//form[@id=\'search\']/div/span/input')
    querybutton_loc=('xpath','//form[@id=\'search\']/div/input')
    assertinsname_loc=('xpath','//tbody/tr/td[1]')


    def click_rechargemanage(self):
        '''点击销售管理'''
        self.click_element(self.rechargemanage_loc)

    def click_inslist(self):
        '''点击客户管理'''
        self.click_element(self.inslist_loc)

    def select_instype(self):
        '''选择测试机构'''
        self.select_by_text(self.instype_loc,'测试机构')

    def input_insname(self):
        '''输入机构名称'''
        self.sendkeys(self.insname_loc,'YP测试机构-于鹏专用')

    def click_querybutton(self):
        '''点击搜索按钮'''
        self.click_element(self.querybutton_loc)

    def assertinsname(self):
        '''验证查询到的机构'''
        insname=self.get_text(self.assertinsname_loc)
        assert insname=='YP测试机构-于鹏专用','查询到的机构不正确'





