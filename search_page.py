# pages/search_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.imdb.com/search/name/"
        self.name_field = (By.ID, "name")
        self.birth_date_field = (By.ID, "birth_date")
        self.death_date_field = (By.ID, "death_date")
        self.gender_dropdown = (By.ID, "gender")
        self.search_button = (By.XPATH, "//button[contains(text(), 'Search')]")
    
    def load(self):
        self.driver.get(self.url)

    def enter_name(self, name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.name_field)
        ).send_keys(name)

    def enter_birth_date(self, birth_date):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.birth_date_field)
        ).send_keys(birth_date)

    def enter_death_date(self, death_date):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.death_date_field)
        ).send_keys(death_date)

    def select_gender(self, gender):
        gender_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.gender_dropdown)
        )
        gender_dropdown.send_keys(gender)

    def click_search(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button)
        ).click()
