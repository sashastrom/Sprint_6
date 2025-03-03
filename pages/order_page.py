from data.locators import *
import allure
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step("Принятие cookie")
    def click_cookie_accept(self):
        self.click(MainPageLocators.cookies_accept)

    @allure.step("Заполняем форму заказа")
    def fill_order_form(self, first_name, last_name, address, subway, telephone, date, rental_period, color, comment_for_courier):

        self.send_keys(OrderPageLocators.first_name, first_name)
        self.send_keys(OrderPageLocators.last_name, last_name)
        self.send_keys(OrderPageLocators.address, address)
        self.click(OrderPageLocators.subway)
        self.click(OrderPageLocators.subway_dropdown(subway))
        self.send_keys(OrderPageLocators.telephone, telephone)
        self.click(OrderPageLocators.next_button)
        self.send_keys(OrderPageLocators.date_field, date)
        self.click(OrderPageLocators.rental_period_field)
        rental_date_list = self.find_elements(OrderPageLocators.rental_date_list)
        if rental_period < len(rental_date_list):
            rental_date_list[rental_period].click()
        else:
            raise IndexError(f"Invalid rental period index: {rental_period}. Max index is {len(rental_date_list) - 1}")
        checkboxes = self.find_elements(OrderPageLocators.checkboxes)
        if color < len(checkboxes):
            checkboxes[color].click()
        else:
            raise IndexError(f"Invalid color index: {color}. Max index is {len(checkboxes) - 1}")
        self.send_keys(OrderPageLocators.comment_for_courier, comment_for_courier)

    @allure.step('Нажимаем "Заказать"')
    def click_order_button(self):
        self.click(OrderPageLocators.order_button)

    @allure.step('Подтвердить заказ-ДА')
    def click_accept_order_yes(self):
        self.click(OrderPageLocators.accept_order_yes_button)

    @allure.step('Получаем сообщение об успешном заказе')
    def get_success_message(self):
        return self.find_element(OrderPageLocators.success_popup).text

    @allure.step('Номер заказа')
    def get_order_number(self):
        about_order_text = self.find_element(OrderPageLocators.order_completed_info).text
        assert 'Номер заказа' in about_order_text

    @allure.step('Видим статус заказа')
    def click_see_order_status(self):
        return self.click(OrderPageLocators.show_status_button)

    @allure.step('Проверка контента о заказе: "Самокат на складе". Кнопка "Отменить заказ" присутствует')
    def check_content_order_page(self):
        element = self.find_element(OrderPageLocators.scooter_in_stock)
        assert 'Самокат на складе' in element.text, f"Текст элемента не совпадает! Найден: {element.text}"
        cancel_button = self.find_elements(OrderPageLocators.cancel_order_button)
        assert len(cancel_button) > 0, "Кнопка 'Отменить заказ' не найдена на странице!"