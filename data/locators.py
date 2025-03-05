from selenium.webdriver.common.by import By


class MainPageLocators:

    cookies_accept = (By.XPATH, ".//button[text()='да все привыкли']")
    order_button_top = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    order_button_bottom = (By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")
    order_status_button = [By.XPATH, ".//button[text()='Статус заказа']"]
    scooter_logo = (By.XPATH, "//img[@src='/assets/scooter.svg' and @alt='Scooter']")
    yandex_logo = (By.XPATH, "//img[@src='/assets/ya.svg' and @alt='Yandex']")


class OrderPageLocators:

    submit_button = (By.XPATH, "//button[contains(text(),'Оформить заказ')]")
    success_popup = (By.XPATH, "//div[contains(text(),'Спасибо')]")
    first_name = (By.XPATH, ".//input[contains(@placeholder,'Имя')]")
    last_name = (By.XPATH, ".//input[contains(@placeholder,'Фамилия')]")
    address = (By.XPATH, ".//input[contains(@placeholder,'Адрес')]")
    subway = (By.XPATH, ".//input[contains(@placeholder,'метро')]")
    telephone = (By.XPATH, ".//input[contains(@placeholder,'Телефон')]")
    next_button = (By.XPATH, ".//button[text()='Далее']")
    back_button = (By.XPATH, ".//button[text()='Назад']")
    date_field = (By.XPATH, ".//input[contains(@placeholder,'Когда')]")

    rental_date_list = (By.XPATH, ".//div[@class='Dropdown-option']")
    rental_period_field = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    checkboxes = [By.XPATH, ".//div[contains(text(),'Цвет')]/parent::div//input"]
    comment_for_courier = [By.XPATH, ".//input[contains(@placeholder,'Комментарий для курьера')]"]
    order_button = [By.XPATH, ".//button[text()='Назад']/parent::div/button[text()='Заказать']"]
    accept_order_yes_button = [By.XPATH, ".//button[text()='Да']"]
    order_completed_info = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
    show_status_button = (By.XPATH, ".//button[text()='Посмотреть статус']")
    scooter_in_stock = (By.XPATH, "//div[@class='Track_Order__1S6E9' and contains(text(), 'Самокат на складе')]")
    cancel_order_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and normalize-space(text())='Отменить заказ']")

    @staticmethod
    def subway_dropdown(subway_name: str):
        return [By.XPATH, f".//div[text()='{subway_name}']/parent::button"]


class FAQPageLocators:

    cookies_accept = (By.XPATH, ".//button[text()='да все привыкли']")
    faq_arrow = (By.XPATH, "//div[contains(@class,'Accordion-module_arrow')]")
    faq_text = (By.XPATH, "//div[contains(@class,'Accordion-module_body')]")

    faq_question_buttons = [
        [By.XPATH, ".//div[@class='accordion__button' and @id='accordion__heading-0']"],
        [By.XPATH, ".//div[@class='accordion__button' and @id='accordion__heading-1']"],
        [By.XPATH, ".//div[@class='accordion__button' and @id='accordion__heading-2']"],
        [By.XPATH, ".//div[@class='accordion__button' and @id='accordion__heading-3']"],
        [By.XPATH, ".//div[@class='accordion__button' and @id='accordion__heading-4']"],
        [By.XPATH, ".//div[@class='accordion__button' and @id='accordion__heading-5']"],
        [By.XPATH, ".//div[@class='accordion__button' and @id='accordion__heading-6']"],
        [By.XPATH, ".//div[@class='accordion__button' and @id='accordion__heading-7']"],
    ]

    faq_answer_texts = [
        [By.XPATH, ".//div[@class='accordion__panel' and @id='accordion__panel-0']/p"],
        [By.XPATH, ".//div[@class='accordion__panel' and @id='accordion__panel-1']/p"],
        [By.XPATH, ".//div[@class='accordion__panel' and @id='accordion__panel-2']/p"],
        [By.XPATH, ".//div[@class='accordion__panel' and @id='accordion__panel-3']/p"],
        [By.XPATH, ".//div[@class='accordion__panel' and @id='accordion__panel-4']/p"],
        [By.XPATH, ".//div[@class='accordion__panel' and @id='accordion__panel-5']/p"],
        [By.XPATH, ".//div[@class='accordion__panel' and @id='accordion__panel-6']/p"],
        [By.XPATH, ".//div[@class='accordion__panel' and @id='accordion__panel-7']/p"],
    ]