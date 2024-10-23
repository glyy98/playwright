from module import *


class   Pageins :

    def __init__(self,page:Page):
        self.page= page
        self.login001= Login_lei(self.page)  #定义login001，引入登录类

