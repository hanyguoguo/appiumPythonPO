#__author__ = 'liuyj'
#coding=utf-8
import os

class GetPath:
    def get_cpath(self):
        #获取当前目录
        # path = os.getcwd()
        path = os.path.abspath(os.path.dirname(__file__))
        return path

    def get_fpath(self):
        #'***获取上级目录***'
        # path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
        # path = os.path.abspath(os.path.dirname(os.getcwd()))
        path = os.path.abspath(os.path.join(os.getcwd(), ".."))
        return path
    def get_gpath(self):
        #获取上上级目录
        path=os.path.abspath(os.path.join(os.getcwd(), "../.."))
        return path


if __name__=="__main__":
    gp = GetPath()
    print gp.get_cpath()
    print gp.get_fpath()
    print gp.get_gpath()