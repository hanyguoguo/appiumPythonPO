#__author__ = 'liuyj'
#coding=utf-8
import yaml

class OperaYaml:
    def __init__(self,file_path=None):
        if file_path==None:
            self.file_path="../config/userconfig.yaml"
        else:
            self.file_path=file_path
        self.data = self.read_data()

    def read_data(self):
        '''
        加载yaml数据
        '''
        with open(self.file_path) as fr:
            data = yaml.load(fr)
        return data

    def get_value(self,user,key):
        '''
        获取user的key的value
        '''
        data =self.read_data()
        value = data[user][key]
        return value

    def write_data(self,i,device,bp,port):
        '''
        写入数据 第i个用户的设备号，bp,port
        '''
        data = self.join_data(i,device,bp,port)
        with open(self.file_path,'a') as fr:
            yaml.dump(data,fr)

    def join_data(self,i,device,bp,port):
        data = {
            "user_info_"+str(i):{
                "deviceName":device,
                "bp":bp,
                "port":port
            }
        }
        return data

    def clear_data(self):
        '''
        清空yamel文件
        '''
        with open(self.file_path,"w") as fr:
            fr.truncate()
        fr.close()

    def get_file_lines(self):
        '''
        获取行数
        '''
        data = self.read_data()
        return len(data)

if __name__=="__main__":
    oy = OperaYaml()
    print oy.get_value('user_info_1','bp')
    print oy.get_file_lines()