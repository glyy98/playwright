from module import *
from module.basepage import PageObject

#PO模式，将元素信息和操作细节封装在page类中
class  Login_lei(PageObject):  #定义一个登录类
    def __init__(self,page):  #定义元素信息
        super().__init__(page)
        self.url ="/#/login"
        self.searchinput_user=self.page.locator('//input[@type="text"]')
        self.searchinput_pwd=self.page.locator('//input[@type="password"]')
        self.searchclick_btn=self.page.get_by_text("登录")
        self.search_pass=self.page.get_by_text("上一跨")

    def login_caozuo(self,search_user,search_pwd): #定义操作细节
        self.navigate() #打开浏览器
        self.searchinput_user.fill(search_user)
        self.searchinput_pwd.fill(search_pwd)
        self.searchclick_btn.click()
        expect(self.search_pass).to_be_visible()

