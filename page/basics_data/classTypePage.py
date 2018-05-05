#-*- coding:utf-8 -*-
#author:yupeng
from common.base import basePage
import time
basics_loc=('css selector','.first.basics')
classtype_loc=('xpath','//a[text()=\'班型\']')
classtype_name='高斯数学五年级能力提高体系（同步青岛54制2课时）'

class classTypePage(basePage):
    '''查询班型'''
    input_classtype_loc=('xpath','//form/div[1]/div[1]/div/div[2]/div/div/input')
    #学科
    subject_loc=('xpath','//form/div[1]/div[3]/div/div[2]/div/div/div/div/div')
    xxsx_loc=('xpath','//li[text()=\'小学数学\']')
    #来源
    laiyuan_loc=('xpath','//form/div[2]/div[2]/div/div[2]/div/div/div/div')
    houtai_loc=('xpath','//li[text()=\'后台\']')
    querybutton_loc=('xpath','//form/div[6]/div/button[1]')
    assertclasstype_loc=('xpath','//table/tbody/tr[1]/td[2]')


    def click_basicsdata(self):
        '''点击基础数据'''
        self.click_element(basics_loc)

    def click_classtype(self):
        '''点击班型'''
        self.click_element(classtype_loc)

    def input_classtypename(self):
        '''输入班型名称'''
        self.sendkeys(self.input_classtype_loc,classtype_name)

    def select_subject(self):
        '''选择学科'''
        self.click_element(self.subject_loc)
        time.sleep(1)
        self.click_element(self.xxsx_loc)

    def select_laiyuan(self):
        '''选择来源'''
        self.click_element(self.laiyuan_loc)
        time.sleep(1)
        self.click_element(self.houtai_loc)

    def click_querybutton(self):
        '''点击查询按钮'''
        self.click_element(self.querybutton_loc)

    def assertclasstype(self):
        result=self.is_text_in_element(self.assertclasstype_loc,classtype_name)
        assert result==True,'班型查询不正确'
