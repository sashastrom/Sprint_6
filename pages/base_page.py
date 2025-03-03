from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.url import Url
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator {locator}")

    def click(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.send_keys(text)

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Переходим по URL')
    def go_to_site(self, url=None):
        if url is None:
            url = Url.main_url
        self.driver.get(url)

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, time=10):
        WebDriverWait(self.driver, time).until(lambda d: len(d.window_handles) > 1)
        current_window = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)
                break
        else:
            raise Exception("Не удалось переключиться на новое окно.")
    def wait_url_until_not_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))