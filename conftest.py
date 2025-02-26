import pytest
from data.url import *
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Url.main_url)
    yield driver
    driver.quit()