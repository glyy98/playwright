from mypy.solve import choose_free
from playwright.sync_api import Page, expect, PageAssertions


def test_login(page:Page):
    page.goto("#/login",wait_until="networkidle") #在500毫秒之内都没新的请求才会退出这个操作
    # page.wait_for_timeout(5000)
    page.locator('//input[@type="text"]').fill("superadmin")
    page.locator('//input[@type="password"]').fill("123456")
    # page.locator('//button[@type="button"]').click()
    page.get_by_text("登录").click()
    expect(page.get_by_text("状态监视")).to_be_visible()
    page.get_by_text("6号").click(click_count=2)  #点击次数
    page.wait_for_timeout(5000)


def test_001(page:Page):
    page.goto("#/login",wait_until="networkidle") #在500毫秒之内都没新的请求才会退出这个操作
    page.locator('//input[@type="text"]').fill("superadmin")
    page.locator('//input[@type="password"]').fill("123456")
    page.get_by_text("登录").click()
    expect(page.get_by_text("状态监视")).to_be_visible()
    page.get_by_text("6号").dblclick() #双击  去6号的整机

    expect(page.get_by_text("参数查询")).to_be_visible()# 会识别到两个6号，因为遍历了下拉框也会识别
    page.wait_for_timeout(2000)
    page.goto("#/liveData/index",wait_until="networkidle") #跳回全局状态
    with page.expect_popup() as  new_page:  #监听跳转到另一台起重机，赋一个新的名称
        page.get_by_text("7号").dblclick()  #跳转到7号
    page_new=new_page.value  #拿到跳转到7号页面的值
    expect(page_new.get_by_text("参数查询"))  #去断言7号页面

def test_task(page:Page):
    page.goto("#/login",wait_until="networkidle") #在500毫秒之内都没新的请求才会退出这个操作
    page.locator('//input[@type="text"]').fill("superadmin")
    page.locator('//input[@type="password"]').fill("123456")
    page.get_by_text("登录").click()
    expect(page.get_by_text("状态监视")).to_be_visible()
    page.get_by_text("任务看板").click()
    page.get_by_text("新建").click(position="x")  #难点：页面有三个新建，一模一样，需要想办法区分

def test_person(page:Page): #悬浮头像后验证账号是否和名称对应
    page.goto("#/login",wait_until="networkidle")
    page.locator('//input[@type="text"]').fill("13960007000")
    page.locator('//input[@type="password"]').fill("123456")
    page.get_by_text("登录").click()

    page.locator('.avatar-img').hover()
    expect(page.get_by_text("小葵花")).to_be_visible()


def test_thing(page:Page): #悬浮头像后验证账号是否和名称对应
    page.goto("#/login",wait_until="networkidle")
    page.locator('//input[@type="text"]').fill("13960007000")
    page.locator('//input[@type="password"]').fill("123456")
    page.get_by_text("登录").click()

    page.get_by_text("历史回放").click()
    expect(page.get_by_text("回放机构状态")).to_be_visible()
    page.locator(".el-select__selection").click()
    page.get_by_text("7号").click()


def test_input001(page:Page): #悬浮头像后验证账号是否和名称对应
    page.goto("#/login",wait_until="networkidle")
    page.locator('//input[@type="text"]').fill("13960007000")
    page.locator('//input[@type="password"]').fill("123456")
    page.get_by_text("登录").click()

    page.get_by_text("任务管理").click()
    page.get_by_text("任务看板").click()
    page.get_by_placeholder("模糊搜索关键词(回车查询)").fill("电源断路器")
    # expect(page.get_by_text("电源断路器")).to_be_visible()
    page.get_by_placeholder("模糊搜索关键词(回车查询)").blur()


def test_plan(page:Page): #悬浮头像后验证账号是否和名称对应
    page.goto("#/login",wait_until="networkidle")
    page.locator('//input[@type="text"]').fill("13960007000")
    page.locator('//input[@type="password"]').fill("123456")
    page.get_by_text("登录").click()

    page.click('//*[@id="sidebar-header"]/div[2]/div[1]/div[2]')
    page.wait_for_timeout(10_000)

    page.get_by_text("新增").click()
    page.get_by_text("请选择",exact=True).click()
    page.get_by_text("5号").click()
    page.get_by_text("请选择设备类型").click()
    page.get_by_text("开关",exact=True).count()
    page.fill('//*[@id="el-id-4305-243"]','点检')
    page.get_by_placeholder("请输入检修方法").fill("method")
    page.get_by_placeholder("请输入检修标准").fill("strand")
    page.get_by_text("司机点检").check()
    expect(page.get_by_text("司机点检")).to_be_checked()



def test_device(page:Page): #悬浮头像后验证账号是否和名称对应
    page.goto("#/health/plant-detail?id=421471904994426949",wait_until="networkidle")
    page.locator('//input[@type="text"]').fill("13960007000")
    page.locator('//input[@type="password"]').fill("123456")
    page.get_by_text("登录").click()
    page.wait_for_timeout(5000)
    page.goto("#/health/plant-detail?id=421471904994426949",wait_until="networkidle")#跳转到设备列表
    # page.wait_for_timeout(2000)
    # page.get_by_placeholder("请搜索设备").fill("再测一次")
    # page.wait_for_timeout(5000)
    page.get_by_text("再测一次",exact=True).click()
    page.get_by_text("上传",exact=True).click()
    page.locator('//input[@type="file"]').set_input_files('pytest.ini')  #上传附件
    expect(page.get_by_text("pytest.ini上传成功")).to_be_visible()
    page.click('.el-dialog__headerbtn') #关闭上传附件的弹窗

    #pw给的方法
    # page.get_by_text("上传",exact=True).click()
    # with page.expect_file_chooser() as chooser:
    #     page.locator(".upload-demo").click()
    # page.wait_for_timeout(5000)
    # chooser.value.set_files('pytest.ini')




def test_role (page:Page):
    page.goto("#/health/plant-detail?id=421471904994426949",wait_until="networkidle")
    page.locator('//input[@type="text"]').fill("13960007000")
    page.locator('//input[@type="password"]').fill("123456")
    page.get_by_text("登录").click()
    page.get_by_text("关闭").click()
    expect(page.get_by_role("dialog",)).to_be_visible() #常见用来断言，主要是触发后的弹窗
    page.get_by_role("checkbox",name="全部",checked=True).count()
    page.get_by_role("dialog").highlight()  #对角色组件进行高亮
    #如果页面中出现多个相同的组件，怎么去定位
    #观察html中的相同的low或者其他词语，定位出来用count看看是不是预期的数量，然后再去细化定位后进行操作
    page.locator(".panel").filter(has_text="维修").get_by_text("新建").click()
    expect(page.get_by_text("新建任务")).to_be_visible()
    expect(page.locator(".panel")).to_have_count(3)
    page.get_by_label("项目").fill("测试")   #适用于没有提示文字的表单输入框

    page.get_by_placeholder("回车查询").fill("666")
    page.keyboard.press('Enter')


#先

















