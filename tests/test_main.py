from conftest import *
from data.tests_data import ClientOrderData
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.url import *
import allure


class TestMainPage:

    @allure.title('Заполнение 1-го набора данных. Проверяем кнопку "Заказать" вверху страницы')
    @allure.description('Проверяем, что при корректном заполнении данных и нажатии на кнопку "Заказать", '
        'происходит успешное оформление заказа, открывается модальное окно с подтверждением об успешном заказе.')

    @pytest.mark.parametrize("order_data", [ClientOrderData.order_details['first_order_set']])
    def test_order_top_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.click_cookie_accept()
        main_page.click_order_button_top()
        order_page = OrderPage(driver)
        order_page.fill_user_data(order_details=order_data)
        order_page.go_next()
        order_page.fill_rent_data(order_details=order_data)
        order_page.click_order_button()
        order_page.click_accept_order_yes()
        order_page.get_order_number()
        order_page.click_see_order_status()
        order_page.check_content_order_page()
        main_page.click_scooter_logo()


    @allure.title('Заполнение 2-го набора данных. Проверяем кнопку "Заказать" внизу страницы')
    @allure.description('Проверяем, что при корректном заполнении данных и нажатии на кнопку "Заказать", '
        'происходит успешное оформление заказа, открывается модальное окно с подтверждением об успешном заказе.')

    @pytest.mark.parametrize("order_data", [ClientOrderData.order_details['second_order_set']])
    def test_order_bottom_button(self, driver, order_data):
        main_page = MainPage(driver)
        main_page.click_cookie_accept()
        main_page.click_order_button_bottom()
        order_page = OrderPage(driver)
        order_page.fill_user_data(order_details=order_data)
        order_page.go_next()
        order_page.fill_rent_data(order_details=order_data)
        order_page.click_order_button()
        order_page.click_accept_order_yes()
        order_page.get_order_number()
        order_page.click_see_order_status()
        order_page.check_content_order_page()



    @allure.title('Яндекс лого - открывает Дзен')
    @allure.description('Проверяем: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.')
    def test_click_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.click_cookie_accept()
        main_page.click_yandex_logo()
        main_page.switch_window()
        main_page.wait_url_until_not_blank()
        current_url = main_page.get_current_url()
        assert (Url.main_url in current_url) or (Url.yandex_dzen_page in current_url) or (
                    Url.yandex_page in current_url), \
            f"Ожидался URL, содержащий один из: {Url.main_url}, {Url.yandex_dzen_page}, {Url.yandex_page}, но найден: {current_url}"