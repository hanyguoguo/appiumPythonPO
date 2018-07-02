#__author__ = 'liuyj'
#coding=utf-8
import ConfigParser
import os

class ReadIni:
    #读取ini文件
    def __init__(self,file_path=None):

        if file_path==None:
            self.file_path = os.path.abspath(os.path.join(os.getcwd(),"../config/LocalElement.ini"))
        else:
            self.file_path=file_path
        self.data = self.read_ini()

    def read_ini(self):
        #读取ini文件，返回数据内容
        read_ini = ConfigParser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    def get_value(self,key,section=None):
        #根据key获取对应的value值
        if section==None:
            section='hospital_login'
        try:
            value= self.data.get(section,key)
        except:
            value=None
        return value

if __name__=="__main__":
    read_ini = ReadIni()
    print read_ini.file_path
    print read_ini.get_value("clinicname")
    print "E:\\pyAppium\\appiumPythonPO\\config\\LocalElement.ini"

