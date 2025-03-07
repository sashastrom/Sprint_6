Final UI test project using POM model after Sprint 6
Project: https://qa-scooter.praktikum-services.ru/

Using:
* FireFox browser 
* Allure Report
* POM
* Selenium
* Pytest

Requirements for testing:

*********  FAQ  *********
- Check dropdown menu in the 'Important Questions' section.
- Need to check: when you click on the arrow, the corresponding text opens.
- It's important to write a separate test for each question.


*********  Order Scooter  *********
- Order of the scooter: You need to check the entire flow of the positive scenario with two sets of data.
- Check the entry points in the scenario. 
- There are two points: the 'Order' button at the top of the page and at the bottom.


*********  Positive scenario testing check list  *********

What the positive scenario consists of:

1. Click the 'Order' button. There are two order buttons on the page.
2. Fill out the order form.
3. Check that a pop-up window appears with a message confirming the successful creation of the order.
4. Check: if you click on the 'Scooter' logo, it takes you to the main page of 'Scooter'.
5. Check: if you click on the Yandex logo, the main page of Zen opens in a new window via redirect.

