from data.locators import *
import allure
from pages.base_page import BasePage



class OrderPage(BasePage):

    @allure.step("Принятие cookie")
    def click_cookie_accept(self):
        self.click(MainPageLocators.cookies_accept)

    @allure.step('Ввод имя')
    def input_first_name(self, first_name: str):
        return self.find_element(OrderPageLocators.first_name).send_keys(first_name)

    @allure.step('Ввод фамилия')
    def input_last_name(self, last_name: str):
        return self.find_element(OrderPageLocators.last_name).send_keys(last_name)

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        return self.find_element(OrderPageLocators.address).send_keys(address)

    @allure.step('Выбор метро')
    def choose_subway(self, subway: str):
        self.find_element(OrderPageLocators.subway).click()
        return self.find_element(OrderPageLocators.subway_dropdown(subway)).click()

    @allure.step('Ввод номера телефона')
    def input_telephone_number(self, telephone: str):
        return self.find_element(OrderPageLocators.telephone).send_keys(telephone)

    @allure.step('Перейти на следующий этап заказа')
    def go_next(self):
        return self.find_element(OrderPageLocators.next_button).click()

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        return self.find_element(OrderPageLocators.date_field).send_keys(date)

    @allure.step('Выбор периода аренды')
    def choose_rental_period(self, option: int):
        self.find_element(OrderPageLocators.rental_period_field).click()
        return self.find_elements(OrderPageLocators.rental_date_list)[option].click()

    @allure.step('Выбор цвета')
    def choose_color(self, option: int):
        return self.find_elements(OrderPageLocators.checkboxes)[option].click()

    @allure.step('Комментарий для курьера')
    def input_comment(self, comment_for_courier):
        return self.find_element(OrderPageLocators.comment_for_courier).send_keys(comment_for_courier)

    @allure.step('Заполнение личных данных Для Кого Самокат')
    def fill_user_data(self, order_details: dict):
        self.input_first_name(order_details['first_name'])
        self.input_last_name(order_details['last_name'])
        self.input_address(order_details['address'])
        self.choose_subway(order_details['subway'])
        self.input_telephone_number(order_details['telephone_number'])

    @allure.step('Заполнить данные Про Аренду')
    def fill_rent_data(self,order_details: dict):
        self.input_date(order_details['date'])
        self.choose_rental_period(order_details['rental_period'])
        for option in order_details['color']:
            self.choose_color(option)
        self.input_comment(order_details['comment_for_courier'])


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