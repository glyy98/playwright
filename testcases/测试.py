from testcases import *

def test_login(page:Page): #

    my_page=Pageins(page)  #引入封装好的登录
    my_page.login001.login_caozuo("superadmin","123456")  #调用登录类中的登录操作细节（方法）


