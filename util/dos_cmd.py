#__author__ = 'liuyj'
#coding=utf-8
import os
class DosCmd:
    def excute_cmd_result(self,command):
    #执行dos命令并获取结果
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':#去掉空行
                continue
            result_list.append(i.strip('\n'))#去掉行尾的换行符
        return result_list

    def excute_cmd(self,command):
    #只执行dos命令不返回结果
        os.system(command)



if __name__=="__main__":
    dos = DosCmd()
    print dos.excute_cmd_result('adb devices')
    dos.excute_cmd('appium -p 4727')