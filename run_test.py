#-*- coding:utf-8 -*-
#author:yupeng
from common.HTMLTestRunner_PY3 import HTMLTestRunner
import time
import unittest
import os

test_path=os.path.dirname(os.path.realpath(__file__))
guanli_case_path=os.path.join(test_path,'guanli-case') ## 测试用例的路径
axx_case_path=os.path.join(test_path,'case') ## 测试用例的路径
report_path=os.path.join(test_path,'report') #报告路径

if __name__=='__main__':
    discover1=unittest.defaultTestLoader.discover(axx_case_path,pattern='test.py')
    #print(type(discover1))
    #discover2=unittest.defaultTestLoader.discover(axx_case_path,pattern='*test.py')

    # all_test=unittest.TestSuite
    # for i in discover1:
    #     all_test.addTest(i)
    # for j in discover2:
    #     all_test.addTest(j)
    # print(all_test)
    nowtime=time.strftime("%Y_%m_%d_%H_%M_%S")
    reportpath=report_path+"\\report%s.html"%nowtime

    with open(reportpath,'wb') as report:
        runner=HTMLTestRunner(report,
                              verbosity=2,
                              title="这是我的报告",
                              description="测试报告")

        runner.run(discover1)

