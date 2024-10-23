from lib2to3.fixes.fix_input import context

from testcases import  *

#更新钥匙
def test_storage_update(page:Page):
    my_page=Pageins(page)
    my_page.login001.login_caozuo("superadmin","123456")
    my_page.page.context.storage_state(path="./storage.json")
    # 以上三行主要是为了拿到登录的鉴权信息，并且将鉴权信息保存在文件中


def test_storage(browser:Browser):
    context=browser.new_context(storage_state="./storage.json")
    page=context.new_page()
    page.goto("https://dev.mhiiot.cn/#/drivingSafety/index")

