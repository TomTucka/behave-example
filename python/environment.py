import os
from selenium import webdriver
from pages import pages

chromedriver = '/usr/local/bin/chromedriver'
def before_scenario(context, scenario):
    context.driver = webdriver.Chrome(chromedriver)
    #context.driver.set_window_size(1024, 768)
    context.is_local = os.environ.get("LOCAL", False) == "true"


def after_scenario(context, scenario):
    context.driver.quit()


def get_url(context, page_name):
    return pages[page_name]
