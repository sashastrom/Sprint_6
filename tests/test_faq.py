import allure
from pages.faq_page import FaqMainPage
from data.tests_data import FagDropdownAnswers
from conftest import *


class TestFAQPage:

    @allure.title("Проверяем выпадающий список в разделе «Вопросы о важном»")
    @allure.description("Kогда нажимаешь на стрелочку, открывается соответствующий текст")
    @pytest.mark.parametrize(
        "question_number, expected_answer",
        [
            (0, FagDropdownAnswers.answer_0),
            (1, FagDropdownAnswers.answer_1),
            (2, FagDropdownAnswers.answer_2),
            (3, FagDropdownAnswers.answer_3),
            (4, FagDropdownAnswers.answer_4),
            (5, FagDropdownAnswers.answer_5),
            (6, FagDropdownAnswers.answer_6),
            (7, FagDropdownAnswers.answer_7),
        ]
    )
    @allure.title('Проверяем что {question_number} сооветсвует ответ {expected_answer}')
    def test_faq_answers(self, driver, question_number, expected_answer):

        faq_page = FaqMainPage(driver)
        faq_page.click_cookie_accept()
        faq_page.click_faq_question(question_number)
        actual_answer = faq_page.get_faq_answer_text(question_number)
        assert actual_answer == expected_answer, f"Ответ на вопрос {question_number} не совпадает. Ожидался: {expected_answer}, Получено: {actual_answer}"