import allure
from data.locators import *

class FaqMainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Принятие cookie")
    def click_cookie_accept(self):
        self.driver.find_element(*FAQPageLocators.cookies_accept).click()


    @allure.step("Клик по вопросу FAQ №{question_number}")
    def click_faq_question(self, question_number):
        faq_arrow = self.driver.find_element(*FAQPageLocators.faq_question_buttons[question_number])
        faq_arrow.click()


    @allure.step("Получаем текст ответа на вопрос {answer_number}")
    def get_faq_answer_text(self, answer_number):
        faq_answer = self.driver.find_element(*FAQPageLocators.faq_answer_texts[answer_number])
        return faq_answer.text.strip()