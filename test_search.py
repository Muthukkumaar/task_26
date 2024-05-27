# tests/test_search.py

import pytest
from selenium import webdriver
from pages.search_page import SearchPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # You can specify the path to your ChromeDriver if it's not in PATH
    yield driver
    driver.quit()

def test_imdb_search(driver):
    search_page = SearchPage(driver)
    search_page.load()
    search_page.enter_name("John Doe")
    search_page.enter_birth_date("01-01-1970")
    search_page.enter_death_date("01-01-2020")
    search_page.select_gender("Male")
    search_page.click_search()

    # Add assertions to verify search results if needed
