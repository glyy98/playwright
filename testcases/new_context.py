from testcases import  *


def test_context(new_context):
    context:BrowserContext=new_context(storage_state="./storage.json")
    context.new_page().goto("#/health/crane")



@pytest.mark.browser_context_args(storage_state="./storage.json")
def test_context_fix(page:Page):

    page.goto("#/health/crane")

