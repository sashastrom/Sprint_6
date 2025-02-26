from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.locators import *
import allure


class MainPage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step("Принятие cookie")
    def click_cookie_accept(self):
        self.driver.find_element(*MainPageLocators.cookies_accept).click()


    @allure.step('Кнопка заказа вверху страницы')
    def click_order_button_top(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.order_button_top)).click()


    @allure.step('Кнопка заказа внизу страницы')
    def click_order_button_bottom(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.order_button_bottom)).click()


    @allure.step('Клик на лого "самокат".Проверяем: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def click_scooter_logo(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.scooter_logo)).click()
        main_url = 'https://qa-scooter.praktikum-services.ru/'
        WebDriverWait(self.driver, 10).until(EC.url_to_be(main_url))
        assert self.driver.current_url == main_url, f"Текущий URL: {self.driver.current_url}, ожидался: {main_url}"


    @allure.step('Клик на лого "Yandex"')
    def click_yandex_logo(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(MainPageLocators.yandex_logo)).click()


    @allure.step('Переключиться на вкладку браузера. Проверяем: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def switch_window(self):
        current_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        print(f"Окна после клика: {len(self.driver.window_handles)}")
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)
                break
    def wait_url_until_not_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))


    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url