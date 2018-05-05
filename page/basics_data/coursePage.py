#-*- coding:utf-8 -*-
#author:yupeng
from selenium import webdriver
from common.base import basePage
import time

basics_loc=('css selector','.first.basics')
course_loc=('xpath','//a[text()=\'课程（新）\']')
coursename='小学数学能力强化体系2课时'

class coursePage(basePage):
    coursename_loc=('css selector','.ant-input')
    subject_loc=('xpath','//form/div[2]/div[1]/div/div[2]/div/div/div/div')
    xxsx_lic=('xpath','//li[text()=\'小学数学\']')
    querybutton_loc=('css selector','.ant-btn.ant-btn-primary')
    assertcourse_loc=('xpath','//tbody/tr/td[2]')

    def click_basicsdata(self):
        '''点击基础数据'''
        self.click_element(basics_loc)

    def click_coursenew(self):
        '''点击课程新'''
        self.click_element(course_loc)

    def input_coursename(self):
        '''输入课程名称'''
        self.sendkeys(self.coursename_loc,coursename)

    def select_subject(self):
        '''选择学科'''
        self.click_element(self.subject_loc)
        time.sleep(1)
        self.click_element(self.xxsx_lic)

    def click_querybutton(self):
        '''点击查询按钮'''
        self.click_element(self.querybutton_loc)

    def assertcourse(self):
        result=self.is_text_in_element(self.assertcourse_loc,coursename)
        assert result==True,'课程与预期不符'



