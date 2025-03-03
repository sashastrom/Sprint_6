import allure
from data.locators import *
from pages.base_page import BasePage

class FaqMainPage(BasePage):

    @allure.step("Принятие cookie")
    def click_cookie_accept(self):
        self.click(FAQPageLocators.cookies_accept)


    @allure.step("Клик по вопросу FAQ №{question_number}")
    def click_faq_question(self, question_number):
        self.click(FAQPageLocators.faq_question_buttons[question_number])


    @allure.step("Получаем текст ответа на вопрос {answer_number}")
    def get_faq_answer_text(self, answer_number):
        faq_answer = self.find_element(FAQPageLocators.faq_answer_texts[answer_number])
        return faq_answer.text.strip()