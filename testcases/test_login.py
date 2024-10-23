from module.Loginpage import Login_lei
from testcases import *

def test_login(page:Page): #
    login_page= Login_lei(page)  #实例化
    login_page.login_caozuo("superadmin","123456")
