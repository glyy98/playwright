from module import *

#封装最基本的代码
class PageObject:
    def __init__(self, page:Page):
        self.page=page
        self.url=''

    def navigate(self):   #登录代码
        self.page.goto(self.url)

    def click_button(self, button_name,timeout=30): #点击按钮
        self.page.get_by_role("button").filter(has_text=button_name).click(timeout=timeout)

