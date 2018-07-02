# coding=utf-8
import sys

sys.path.append("E:/pyAppium/appiumPythonPO")
import unittest
import HTMLTestRunner
import threading
import multiprocessing
from util.sever import Server
import time
from appium import webdriver
from business.login_business import LoginBusiness
from util.opera_yaml import OperaYaml


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class CaseTest(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print "setUpclass---->", parames
        cls.login_business = LoginBusiness(parames)
        # cls.driver=cls.login_business.login_handle.login_page.driver()

    def setUp(self):
        print "this is setup\n"

    def test_01(self):
        print "this is case01\n"
        self.login_business.login_pass()


    def test_02(self):
        print "this is case02\n"
        self.login_business.login_user_error()
        self.assertTrue(True)

    def tearDown(self):
        time.sleep(1)
        print "this is teardown\n"
        #如果报错就截图
        if sys.exc_info()[0]:
            self.login_business.login_handle.login_page.driver.save_screenshot("../jpg/test02.png")

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        print "this is class teardown\n"
        # cls.driver.quit()


def appium_init():
    server = Server()
    # server.main_threads()
    server.main_process()


def get_suite(i):
    print u"get_suite里面的", i
    suite = unittest.TestSuite()
    suite.addTest(CaseTest("test_02", parame=i))
    suite.addTest(CaseTest("test_01", parame=i))

    # unittest.TextTestRunner().run(suite)
    html_file = '..\\report\\report_' + str(i) + ".html"
    fp = file(html_file, "wb")
    HTMLTestRunner.HTMLTestRunner(stream=fp).run(suite)


def get_count():
    write_user_file = OperaYaml()
    count = write_user_file.get_file_lines()
    return count


if __name__ == '__main__':
    appium_init()
    processes = []
    for i in range(get_count()):
        print i
        t = multiprocessing.Process(target=get_suite, args=(i,))
        processes.append(t)
    for p in processes:
        p.start()
        time.sleep(30)
