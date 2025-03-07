from conftest import *
from data.locators import OrderPageLocators
from data.tests_data import ClientOrderData
from pages.order_page import OrderPage
from data.url import *
import allure


class TestOrder:

    @allure.title('Заполнение корректных данных и переход с 1-ого этапа на 2-ую страницу')
    @allure.description('Проверяем что при корректно заполненных данных "Для Кого Самокат", '
                        'и нажатии кнопки "Далее" переходим на 2-ую страницу Про Аренду')
    def test_correct_input_order_data_for_client_first_page(self,driver):
        order_page = OrderPage(driver)
        order_page.go_to_site(Url.order_url)
        order_page.click_cookie_accept()
        order_page.fill_user_data(order_details=ClientOrderData.order_details['first_order_set'])
        order_page.go_next()
        assert len(order_page.find_elements(OrderPageLocators.order_button))>0

    @allure.title('Заполнение корректных данных на 2-ой странице и успешное оформление заказа')
    @allure.description('Проверяем что при корреткно заполненных данных Про Аренду, '
                        'и нажатии кнопки "Заказать", заказ оформлен, видим модальное окно '
                        'с подтверждением об успешном заказе и его номером')

    @pytest.mark.parametrize('order_details', ['first_order_set', 'second_order_set'])
    def test_proceeding_success_order_second_page_show_order_number_success(self, driver, order_details):
        order_page = OrderPage(driver)
        order_page.go_to_site(Url.order_url)
        order_page.click_cookie_accept()
        order_page.fill_user_data(order_details=ClientOrderData.order_details[order_details])
        order_page.go_next()
        order_page.fill_rent_data(order_details=ClientOrderData.order_details[order_details])
        order_page.click_order_button()
        order_page.click_accept_order_yes()
        assert len(order_page.find_elements(OrderPageLocators.order_completed_info))>0

    @allure.title('Оформление заказа и переход на страницу с заказом')
    @allure.description('Проверяем успешное оформлении заказа, заказ отображается на странице "Статус заказа"')
    @pytest.mark.parametrize('order_details', ['first_order_set', 'second_order_set'])
    def test_create_order_and_get_order_status(self, driver, order_details):
        order_page = OrderPage(driver)
        order_page.go_to_site(Url.order_url)
        order_page.click_cookie_accept()
        order_page.fill_user_data(order_details=ClientOrderData.order_details[order_details])
        order_page.go_next()
        order_page.fill_rent_data(order_details=ClientOrderData.order_details[order_details])
        order_page.click_order_button()
        order_page.click_accept_order_yes()
        order_page.get_order_number()
        order_page.click_see_order_status()
        order_page.check_content_order_page()