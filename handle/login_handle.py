# coding=utf-8
from page.login_page import LoginPage
from util.sever import Server

class LoginHandle:
    def __init__(self, i):
        self.login_page = LoginPage(i)

    # 操作登录页面的元素
    def send_username(self, user):
        '''
        输入用户名
        '''
        self.login_page.get_username_element().send_keys(user)

    def send_password(self, password):
        '''
        输入密码
        '''
        self.login_page.get_password_element().send_keys(password)

    def click_login(self):
        '''
        点击登录按钮
        '''
        self.login_page.get_login_button_element().click()

    def click_forget_password(self):
        '''
        点击忘记密码
        '''
        self.login_page.get_forget_password_element().click()

    def click_rember(self):
        '''
        点击记住密码
        '''
        self.login_page.get_remember_password_element().click()

    def get_fail_tost(self, message):
        '''
        获取tost，根据返回信息进行反数据
        '''
        return self.login_page.find_toast(message)
        # tost_element = self.login_page.get_tost_element(message)
        # if tost_element:
        #     return True
        # else:
        #     return False

if __name__=="__main__":
    hl=LoginHandle(0)
    hl.send_username('13051852488')
    # hl.send_password('111111')
    hl.click_login()
    print hl.get_fail_tost('请输入6-8位密码')
