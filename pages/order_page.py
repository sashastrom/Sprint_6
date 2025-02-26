from data.locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Принятие cookie")
    def click_cookie_accept(self):
        self.driver.find_element(*MainPageLocators.cookies_accept).click()

    @allure.step("Заполняем форму заказа")
    def fill_order_form(self, first_name, last_name, address, subway, telephone, date, rental_period, color, comment_for_courier):

        self.driver.find_element(*OrderPageLocators.first_name).send_keys(first_name)
        self.driver.find_element(*OrderPageLocators.last_name).send_keys(last_name)
        self.driver.find_element(*OrderPageLocators.address).send_keys(address)
        self.driver.find_element(*OrderPageLocators.subway).click()
        self.driver.find_element(*OrderPageLocators.subway_dropdown(subway)).click()
        self.driver.find_element(*OrderPageLocators.telephone).send_keys(telephone)
        self.driver.find_element(*OrderPageLocators.next_button).click()
        self.driver.find_element(*OrderPageLocators.date_field).send_keys(date)
        self.driver.find_element(*OrderPageLocators.rental_period_field).click()
        rental_date_list = self.driver.find_elements(*OrderPageLocators.rental_date_list)
        if rental_period < len(rental_date_list):
            rental_date_list[rental_period].click()
        else:
            raise IndexError(f"Invalid rental period index: {rental_period}. Max index is {len(rental_date_list) - 1}")
        checkboxes = self.driver.find_elements(*OrderPageLocators.checkboxes)
        if color < len(checkboxes):
            checkboxes[color].click()
        else:
            raise IndexError(f"Invalid color index: {color}. Max index is {len(checkboxes) - 1}")
        self.driver.find_element(*OrderPageLocators.comment_for_courier).send_keys(comment_for_courier)

    @allure.step('Нажимаем "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()

    @allure.step('Подтвердить заказ-ДА')
    def click_accept_order_yes(self):
        self.driver.find_element(*OrderPageLocators.accept_order_yes_button).click()

    @allure.step('Получаем сообщение об успешном заказе')
    def get_success_message(self):
        return self.driver.find_element(*OrderPageLocators.success_popup).text

    @allure.step('Номер заказа')
    def get_order_number(self):
        about_order_text = self.driver.find_element(*OrderPageLocators.order_completed_info).text
        assert 'Номер заказа' in about_order_text

    @allure.step('Видим статус заказа')
    def click_see_order_status(self):
        return self.driver.find_element(*OrderPageLocators.show_status_button).click()

    @allure.step('Проверка контента о заказе: "Самокат на складе". Кнопка "Отменить заказ" присутствует')
    def check_content_order_page(self):
        element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(OrderPageLocators.scooter_in_stock))
        assert 'Самокат на складе' in element.text, f"Текст элемента не совпадает! Найден: {element.text}"
        cancel_button = self.driver.find_elements(*OrderPageLocators.cancel_order_button)
        assert len(cancel_button) > 0, "Кнопка 'Отменить заказ' не найдена на странице!"