#__author__ = 'liuyj'
#coding=utf-8
from dos_cmd import DosCmd

class Port:
    def port_is_used(self,port):
        '''
        判断端口是否被占用
        '''
        flag=None
        self.dos = DosCmd()
        command ='netstat -ano | findstr'+str(port)
        result = self.dos.excute_cmd_result(command)
        if len(result)>0:
            flag=True
        else:
            flag=False
        return flag

    def create_port_list(self,start_port,devices_list):
        '''
        生成可用端口，传入起始端口号，和设备列表
        '''
        port_list = []
        if devices_list !=None:
            while len(port_list) != len(devices_list):
                if self.port_is_used(start_port)!=True:
                    port_list.append(start_port)
                start_port=start_port+1
            return port_list
        else:
            print u"生成可用端口失败"
            return None

if __name__=="__main__":
    port = Port()
    print port.port_is_used(4725)
    print port.create_port_list(4723,[1,2,3,4,5])