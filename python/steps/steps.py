from behave import when, then
from environment import get_url


@when(u"I am on '{page_name}'")
def impl(context, page_name):
    context.response = context.driver.get(get_url(context, page_name))


@then(u"The page title should be {search_string}")
def impl(context, search_string):
    print(context.driver.title)
    assert search_string == context.driver.title
