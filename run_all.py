#-*- coding:utf-8 -*-
#author:yupeng
import os
import unittest
from common.HTMLTestRunner_PY3 import HTMLTestRunner
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
'''
将整个执行过程分为四步：
1、加载用例
2、执行用例并生成报告
3、取最新生成的测试报告
4、给指定的人发送邮件，附件为测试报告
'''
#加载项目真实路径
auto_path=os.path.dirname(os.path.realpath(__file__))
#1、加载用例
def add_case(caseName,runCaseRule):
    '''1、加载用例'''
    #执行用例的路径
    case_path=os.path.join(auto_path,caseName)
    #discover加载符合规则的用例
    discover=unittest.defaultTestLoader.discover(case_path,
                                                 pattern=runCaseRule,
                                                 top_level_dir=None)
    return discover

#2、执行用例
def run_case(all_case,report_Name):
    '''2、执行用例'''
    now=time.strftime('%Y_%m_%d %H_%M_%S')#时间戳
    report_path=os.path.join(auto_path,report_Name)#加载报告路径
    report=report_path+'\\report%s.html'%now#定义生成报告的格式
    with open(report,'wb') as fp:#打开报告以二进制方式写入内容，并执行
        runner=HTMLTestRunner(fp,
                              verbosity=2,
                              title='自动化测试报告',
                              description='执行自动化用例如下：'
                              )
        runner.run(all_case)#add_case方法返回的值

#3、取最新生成的测试报告
def get_report_file(report_path):
    '''3、取最新生成的测试报告'''
    lists=os.listdir(report_path)#加载报告文件夹中所有的报告
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))#利用时间进行排序 匿名函数
    report_file=os.path.join(report_path,lists[-1])#取排序后报告中的最新一个
    return report_file#将最新报告返回

#4、发送报告
def send_mail(sender,pwd,receiver,smtpserver,report_file,port):
    '''第四步：发送最新的测试报告内容'''
    with open(report_file,'rb') as fp:
        mail_body=fp.read()
    msg=MIMEMultipart()
    body=MIMEText(mail_body,'html','utf-8')
    msg['Subject']='自动化测试报告'
    msg['from']=sender
    msg['to']=','.join(receiver)
    msg.attach(body)
    #添加附件
    att=MIMEText(open(report_file,'rb').read(),'base64','utf-8')
    att['Content-type']='application/octet-stream'
    att['Content-Disposition']='attachment;filename="report.html"'
    msg.attach(att)
    try:
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(sender,pwd)
    except:
        smtp=smtplib.SMTP_SSL(smtpserver,port)
        smtp.login(sender,pwd)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()
    print('邮件已发出')

#组织用例执行并发送报告
if __name__=='__main__':
    all_case=add_case('testCase','test*.py')
    #执行用例
    run_case(all_case,'report')
    #报告路径
    report_path=os.path.join(auto_path,'report')
    #取最新生成的报告
    report_file=get_report_file(report_path)
    #发送报告，必要参数
    sender= '617955991@qq.com'
    pwd= 'pevlpowsdmoibdih'
    smtp_server= 'smtp.qq.com'
    port= 465
    receiver= ["944354642@qq.com",'yupeng0310@126.com','yupeng@gaosiedu.com']
    send_mail(sender,pwd,receiver,smtp_server,report_file,port)

