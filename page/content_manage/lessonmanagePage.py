#-*- coding:utf-8 -*-
#author:yupeng
from common.base import basePage
import time
import os
cur_path=os.path.dirname(os.path.realpath(__file__))
grader_father=os.path.abspath(os.path.dirname(cur_path)+os.path.sep+"..")
file_path=os.path.join(grader_father,'file')
kj_path=os.path.join(file_path,'课件.zip')
sp_path=os.path.join(file_path,'123.mp4')
pdf_path=os.path.join(file_path,'【课程顾问工作流程】.pdf')
kjsc_path=os.path.join(file_path,'upfile_kj.exe')
print(kjsc_path)
class lessonmanagePage(basePage):
    contentmanage_loc=('xpath','//ul/li[3]/a')
    lessonmanage_loc=('xpath','//a[text()=\'课节管理\']')
    subject_loc=('xpath','//a[text()=\'小学英语\']')
    class_loc=('xpath','//a[text()=\'一年级\']')
    managelesson_loc=('xpath','//td[text()="小学英语在线外教测试班型"]/following-sibling::td[contains(text(),"春季班")]/following-sibling::td[*]/a[contains(text(),"管理课节")]')
    #summerclass_loc=('xpath','//td[text()="小学英语在线外教测试班型"]/parent::*/following-sibling::tr[1]/td[contains(text(),"暑假班")]/following-sibling::td[*]/a[text()="管理课节"]')
    #//td[text()="小学英语在线外教测试班型"]/parent::*/following-sibling::tr[2]/td[contains(text(),"秋季班")]/following-sibling::td[*]/a[text()="管理课节"]
    #//td[text()="小学英语在线外教测试班型"]/parent::*/following-sibling::tr[3]/td[contains(text(),"寒假班")]/following-sibling::td[*]/a[text()="管理课节"]
    kj_loc=('xpath','//td[text()="1"]/following-sibling::td[4]/span[2]/a')
    bksp_loc=('xpath','//td[text()="1"]/following-sibling::td[5]/span[2]/a')
    ktsl_loc=('xpath','//td[text()="1"]/following-sibling::td[6]/span[2]/a')
    jsjy_loc=('xpath','//td[text()="1"]/following-sibling::td[7]/span[2]/a')
    tjkj_loc=('xpath','//input[@value="添加课件"]')
    iframe_loc=('jbox-iframe')
    qnsc_loc=('xpath','//input[@id=\'pickfiles\']')
    qdbutton_loc=('xpath','//div[1]/div[4]/input')
    assertkj_loc=('xpath','//tr/td[2]')

    def click_contentmanage(self):
        '''点击内容管理'''
        self.click_element(self.contentmanage_loc)
    def click_lessonmanage(self):
        '''点击课节管理'''
        self.click_element(self.lessonmanage_loc)
    def upfile(self):
        '''上传文件'''
        self.click_element(self.subject_loc)
        self.click_element(self.class_loc)
        self.click_element(self.managelesson_loc)
        self.switchto_window(-1)
        self.click_element(self.kj_loc)
        time.sleep(3)
        self.switchto_frame(self.iframe_loc)
        self.click_element(self.tjkj_loc)
        time.sleep(5)
        self.switchto_frame(self.iframe_loc)
        #self.sendkeys(self.qnsc_loc,kj_path)
        #self.driver.find_element_by_xpath('//div[1]/div[2]/div[1]/input').send_keys(r'F:\gaosi\file\课件.zip')
        self.driver.find_element_by_xpath('//input[@id=\'pickfiles\']').click()
        #os.system("D:\\upfile.exe")
        os.system("F:\\gaosi\\file\\upfile_kj.exe")
        time.sleep(20)
        self.driver.switch_to.parent_frame()
        result=self.is_text_in_element(self.assertkj_loc,"课件")
        print(result)
        self.click_element(self.qdbutton_loc)



