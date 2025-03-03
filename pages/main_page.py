from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.locators import *
import allure
from pages.base_page import BasePage
from data.url import Url


class MainPage(BasePage):


    @allure.step("Принятие cookie")
    def click_cookie_accept(self):
        self.click(MainPageLocators.cookies_accept)


    @allure.step('Кнопка заказа вверху страницы')
    def click_order_button_top(self):
        self.click(MainPageLocators.order_button_top)


    @allure.step('Кнопка заказа внизу страницы')
    def click_order_button_bottom(self):
        self.click(MainPageLocators.order_button_bottom)


    @allure.step('Клик на лого "самокат".Проверяем: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».')
    def click_scooter_logo(self):
        self.click(MainPageLocators.scooter_logo)
        main_url = Url.main_url
        self.wait_url_until_not_blank()
        assert self.driver.current_url == main_url, f"Текущий URL: {self.driver.current_url}, ожидался: {main_url}"


    @allure.step('Клик на лого "Yandex"')
    def click_yandex_logo(self):
        self.click(MainPageLocators.yandex_logo)


    @allure.step('Переключиться на вкладку браузера. Проверяем: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def switch_window_to_new(self):
        current_window = self.driver.current_window_handle
        self.switch_window(current_window)
