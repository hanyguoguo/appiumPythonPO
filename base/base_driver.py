# coding=utf-8
import time
from appium import webdriver
from util import read_init
from util.opera_yaml import OperaYaml


class BaseDriver:

    def android_driver(self, i):
        print "this is android_driver:", i
        write_file = OperaYaml()
        devices = write_file.get_value('user_info_' + str(i), 'deviceName')
        port = write_file.get_value('user_info_' + str(i), 'port')
        capabilities = {
            "platformName": "Android",
            "platforVersion": "6.0.1",
            "automationName":"UiAutomator2",#获取toast需要用
            "deviceName": devices,
            "app": "E:\\pyAppium\\appiumPythonPO\\app-localtest-release.apk",
            "appPackage": "com.hospital.localtest",
            "appWaitActivity": "hospital.com.mainlib.login.LoginActivity",
            "noReset": "true",
            "unicodeKeyboard": "True",
            "resetKeyboard":"True"

        }
        driver = webdriver.Remote("http://127.0.0.1:" + str(port) + "/wd/hub", capabilities)
        time.sleep(15)
        return driver

if __name__=="__main__":
    base_driver=BaseDriver()
    driver =base_driver.android_driver(0)
