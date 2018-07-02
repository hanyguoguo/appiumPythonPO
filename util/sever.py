#__author__ = 'liuyj'
#coding=utf-8
from dos_cmd import DosCmd
from port import Port
import threading
import multiprocessing
import time
from opera_yaml import OperaYaml

class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.device_list = self.get_devices()
        self.opera_yaml = OperaYaml()
    def get_devices(self):
        '''
        获取设备列表
        '''
        print u"生成设备列表"
        devices_list=[]
        result_list = self.dos.excute_cmd_result("adb devices")
        if len(result_list)>=2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1]=='device':
                    devices_list.append(devices_info[0])
            return devices_list

        else:
            return None

    def create_ports(self,start_port):
        '''
        创建可用端口列表
        '''
        print u"生成可用端口列表"
        port = Port()
        port_list =[]
        port_list=port.create_port_list(start_port,self.device_list)
        print port_list
        return port_list

    def create_command(self,i):
        '''
        生成第i 个命令并写入yaml文件
        '''
        #appium -p 4700 -bp 4900 -U XXXX
        command_list=[]
        ap_list = self.create_ports(4700)
        bp_list = self.create_ports(4900)
        device_list = self.device_list
        command = "appium -p "+str(ap_list[i])+" -bp "+str(bp_list[i])+" -U "+device_list[i]+" --no-reset --session-override"
        #--log E:/pyAppium/appiumPythonPO/log/test.log"
        print u"生成第"+str(i)+u"个命令"+command
        command_list.append(command)
        print u"开始写入第"+str(i)+u"个命令"
        self.opera_yaml.write_data(i,device_list[i],str(bp_list[i]),str(ap_list[i]))
        return  command_list

    def start_server(self,i):
        '''
        启动服务
        '''
        self.start_list=self.create_command(i)
        print "start_list:"
        print self.start_list
        self.dos.excute_cmd(self.start_list[0])

    def kill_server(self):
        '''
        停止服务
        '''
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')

    def get_commands_num(self):

        return self.opera_yaml.get_file_lines()

    def main_threads(self):
        #多线程启动服务
        thread_list = []
        self.kill_server()
        self.opera_yaml.clear_data()
        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            thread_list.append(appium_start)
        for j in thread_list:
            j.start()
        time.sleep(25)

    def main_process(self):
        '''
        多进程启动服务
        '''
        #每次启动服务之前，杀死已有的进程
        self.kill_server()
        #每次启动服务之前，清空yaml文件
        self.opera_yaml.clear_data()
        for i in range(len(self.device_list)):
            appium_start = multiprocessing.Process(target=self.start_server, args=(i,))
            appium_start.start()
        time.sleep(25)

    def main(self,i):
        self.kill_server()
        self.opera_yaml.clear_data()
        self.start_server(i)
        time.sleep(20)


if __name__=="__main__":
    server = Server()
    server.main_threads()
