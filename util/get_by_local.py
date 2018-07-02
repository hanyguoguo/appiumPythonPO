#__author__ = 'liuyj'
#coding=utf-8
from read_init import ReadIni
from base.base_driver import BaseDriver

class GetByLocal:
    def __init__(self,driver):
        self.driver=driver

    def get_element(self,key):
        #常用
        read_ini=ReadIni()
        local= read_ini.get_value(key)
        if local !=None:
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                #self.driver.sava_screenshot('../jpg/test.jpg')
                return None
        else:
            return None

if __name__=="__main__":
    bd = BaseDriver()
    driver =bd.android_driver(0)
    gb=GetByLocal(driver)
    print gb.get_element('clinicname').text()
