# coding=utf-8
from handle.login_handle import LoginHandle
from util.sever import Server

class LoginBusiness:
    def __init__(self, i):
        self.login_handle = LoginHandle(i)

    def login_pass(self):
        self.login_handle.send_username('13051852488')
        self.login_handle.send_password('123456')
        self.login_handle.click_login()

    def login_user_error(self):
        print "start login_user_error..."
        self.login_handle.send_username('13051852400')
        self.login_handle.send_password('123456')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost('该账号不存在')
        print user_flag
        if user_flag:
            return True
        else:
            return False

    def login_password_error(self):
        print "start login_pwd_error..."
        self.login_handle.send_username('13051852488')
        self.login_handle.send_password('111112')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_fail_tost('用户名与密码不符')
        print user_flag
        if user_flag:
            return True
        else:
            return False

if __name__=="__main__":
    # server = Server()
    # server.main_process()
    lb=LoginBusiness(0)
    lb.login_user_error()
    lb.login_password_error()
    lb.login_pass()